from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.db.models import Q

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import action
from .models import *
from .serializers import ModelPrinterSerializer, FeatureSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from django_filters import rest_framework as filters



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

class ModelPrinterDetailView(APIView):
    def get_object(self, id):
        try:
            return ModelPrinter.objects.get(id=id)
        except ModelPrinter.DoesNotExist as e:
            return Response( {"error": "Given model object not found."}, status=404)

    def get(self, request, id=None):
        instance = self.get_object(id)
        serailizer = ModelPrinterSerializer(instance)
        return Response(serailizer.data)

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = ModelPrinterSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.erros, status=400)

    def delete(self, request, id=None):
        instance = self.get_object(id)
        instance.delete()
        return HttpResponse(status=204)


