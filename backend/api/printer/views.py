import requests
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.db.models import Q
import base64
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import filters
from rest_framework import permissions
from rest_framework.decorators import action, api_view
from .permissions import IsOwnerAuth, ModelViewSetsPermission
from .models import *
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework.decorators import action
from django.core.files.base import ContentFile
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from rest_framework.mixins import (
    UpdateModelMixin
)

from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
# from django_filters.filters import OrderingFilter as o

from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils.translation import gettext_lazy as _

from django_elasticsearch_dsl_drf.constants import LOOKUP_FILTER_GEO_DISTANCE
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    SearchFilterBackend,
    DefaultOrderingFilterBackend,
)

class ModelPrinterViewSet(viewsets.ModelViewSet):
    serializer_class = ModelPrinterSerializer
    queryset = ModelPrinter.objects.all()
    lookup_field = 'id'
    filter_backends = (DjangoFilterBackend,)
    authentication_classes = (TokenAuthentication,)


    @action(detail=True, methods=["GET"])
    def features(self, request, id=None):
        model = self.get_object()
        features = Feature.objects.filter(model=model)
        serializer = FeatureSerializer(features, many=True)
        return Response(serializer.data, status=200)

    @action(detail=True, methods=["POST"])
    def feature(self, request, id=None):
        model = self.get_object()
        data = request.data
        data["model"] = model.id
        serializer = FeatureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status=400)



class ModelPrinterListView(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    serializer_class = ModelPrinterSerializer
    queryset = ModelPrinter.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]



    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def put(self, request, id=None):
        return self.update(request, id)

    def perform_update(self, serializer):
        print(self.request.user)
        serializer.save(created_by=self.request.user)        

    def delete(self, request, id=None):
        return self.destroy(request, id)



class ModelPrinterAPIView(APIView):
    def get(self, request):
        models = ModelPrinter.objects.all()
        serailizer = ModelPrinterSerializer(models, many=True)
        return Response(serailizer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = ModelPrinterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status=400)


class ListPrinterView(viewsets.ModelViewSet):
    # permission_classes = (ModelViewSetsPermission,)
    serializer_class = CreatePrinterSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ("floor","model_name")
    ordering_fields = ("created_at",'page_remaining',)
    filter_fields = ("status",'model_name')
    queryset = Printer.objects.all()

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     print("queryset -> ", queryset)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer)

    def update(self, request, *args, **kwargs):
        return super(ListPrinterView, self).update(request, *args, **kwargs)
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        printers = Printer.objects.all()
        serializer = PrinterSerializer(printers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PrinterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FloorListAPIView(ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = FloorSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ("floor_code",)
    filter_fields = ("building_code",)
    # queryset = Floor.objects.all()

    def get_queryset(self):
        queryset = Floor.objects.all()
        return queryset


class FloorAPIView(RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = FloorSerializer
    queryset = Floor.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)

class UpdatePagesRemainingAPIView(APIView):
    def get_object(self, pk):
        try:
            return Printer.objects.get(pk=pk)
        except Printer.DoesNotExist:
            return None

    def patch(self, request, pk):
        printer = self.get_object(pk)
        if printer:
            # Update pages_remaining by adding 200 to the current value
            printer.pages_remaining += 200
            printer.save()

            # Serialize the updated printer and return the response
            serializer = PrinterSerializer(printer)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"detail": "Printer not found"}, status=status.HTTP_404_NOT_FOUND)
    
class ListPrinterAPIView(ListAPIView):
    serializer_class = PrinterSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    search_fields = ("floor_description",)
    ordering_fields = ("created_at",) # change related at to time remaining
    filter_fields = ("status",)
    queryset = Printer.objects.all()

    # Cache requested url for each user for 2 hours
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class CreatePrinterAPIView(CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = CreatePrinterSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=user)
        # push_notifications(user, request.data["title"], "you have add a new printer")
        # if user.profile.phone_number:
        #     send_message(user.profile.phone_number, "Congratulations, you Created New Printer")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
# class UpdatePrinterAPIView(UpdateModelMixin):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = UpdatePrinterSerializer

#     def put(self, request,*args, **kwargs ):
#         user = request.user
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#                 serializer.save(modified_by = user)
#                 return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DestroyPrinterAPIView(DestroyAPIView):
    permission_classes = [IsOwnerAuth]
    serializer_class = PrinterDetailSerializer
    queryset = Printer.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({"detail": "Printer deleted"})

class PrinterDetailView(APIView):
    def get(self, request, pk):
        printer = self.get_object(id = pk)
        if printer:
            serializer = PrinterSerializer(printer)
            return Response(serializer.data)
        return Response({"detail": "Printer not found"}, status=status.HTTP_404_NOT_FOUND)
    def update(self, request, pk):
        printer = self.get_object(id=pk)
        if printer:
            # Use a serializer that only allows updating 'status' and 'pages_remaining'
            serializer = UpdatePrinterSerializer(printer, data=request.data, partial=True)
            if serializer.is_valid():
                user = request.user
                serializer.save(modified_by= user)
                
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Printer not found"}, status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk):
        printer = self.get_object(id = pk)
        if printer:
            serializer = PrinterSerializer(printer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Printer not found"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, pk):
        printer = self.get_object(id = pk)
        if printer:
            # Change status to Offline instead of deleting
            printer.status = Printer.OFFLINE
            printer.save()
            return Response({"detail": "Printer set to Offline"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Printer not found"}, status=status.HTTP_404_NOT_FOUND)

class FileUploadView(APIView):
    def get(self, request, format=None):
        file_upload_data = request.session.get('file_upload_data', None)

        if file_upload_data is None:
            # Provide a default response when session data is not found
            default_response = {"message": "Session data not available"}
            return Response(default_response)

        response_data = {
            "file_upload_data": {
                "file_upload": file_upload_data.get('file_upload'),
                "pagenumber": file_upload_data.get('pagenumber'),
            },
        }
        return Response(response_data)

    def post(self, request, format=None):
        serializer = FileuploadSerializer(data=request.data)

        if serializer.is_valid():
            # Store file information in the session
            file_upload = request.FILES['file_upload']
            file_upload_data = {
                'file_upload': {
                    'name': file_upload.name,
                    'size': file_upload.size,
                    'content_type': file_upload.content_type,
                    'base64_content': base64.b64encode(file_upload.read()).decode('utf-8'),
                },
                'pagenumber': serializer.validated_data['pagenumber'],
            }
            request.session['file_upload_data'] = file_upload_data
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrinterOrderView(APIView):
    def get(self, request, format=None):
        file_upload_data = request.session.get('file_upload_data', None)

        if not file_upload_data or not file_upload_data.get('file_upload'):
            return Response({"error": "File upload data not found"}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve printers with pageremaining > pagenumber
        printers = Printer.objects.filter(pages_remaining__gte=file_upload_data['pagenumber'])

        # Serialize the printers
        printer_serializer = PrinterSerializer(printers, many=True)

        # Include file information in the response
        response_data = {
            "file_upload_data": {
                "file_upload": file_upload_data['file_upload'],
                "pagenumber": file_upload_data['pagenumber'],
            },
            "printers": printer_serializer.data,
        }

        return Response(response_data)

    def post(self, request, format=None):
        file_upload_data = request.session.get('file_upload_data', None)

        if not file_upload_data or not file_upload_data.get('file_upload'):
            return Response({"error": "File upload data not found"}, status=status.HTTP_400_BAD_REQUEST)

        base64_content = file_upload_data['file_upload']['base64_content']

        # Giải mã nội dung từ Base64
        decoded_content = base64.b64decode(base64_content)

        file_name = file_upload_data['file_upload']['name']
        file_size = file_upload_data['file_upload']['size']
        content_type = file_upload_data['file_upload']['content_type']
        file_content = ContentFile(decoded_content, name=file_name)
        submitdata = request.data
        submitdata['file_upload'] = file_content

        # Serialize the request data using OrderPrinterSerializer
        serializer = OrderPrinterSerializer(data=submitdata)

        if serializer.is_valid():
            # Create a new print order
            order_printer = serializer.save()

            # Update the corresponding printer's pages_remaining
            printer_id = int(request.data.get('printer'))
            printer = Printer.objects.get(pk=printer_id)
            printer.pages_remaining -= int(request.data.get('pages'))
            printer.save()



            # Return a success response
            return Response({"message": "Print order submitted successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)

        else:
            # Return an error response if the serializer data is invalid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)