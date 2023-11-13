from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets, permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import reverse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from api.auth.models import Person, User
from .models import Student, Officer
from .serializers import StudentSerializer, OfficerSerializer

from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

class StudentProfileViewSet(viewsets.ViewSet, permissions.BasePermission):
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes=[permissions.AllowAny]
    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Student.objects.filter(user_id = request.user.id)

        serializer = StudentSerializer(queryset)
        return Response(serializer.data)

    
    # def get_permissions(self):
    #     if self.action == 'list':
    #         # Allow read-only access for list action
    #         return [permissions.AllowAny()]
    #     elif self.action == 'get':
    #         pass
    #     else:
    #         pass
    #     return super().get_permissions()
student_list = StudentProfileViewSet.as_view({'get':'list'})
studnet_detail = StudentProfileViewSet.as_view({'get':'retrieve'})

class OfficerProfileViewSet(viewsets.ViewSet):
    serializer_class = OfficerSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes=[permissions.AllowAny]
    
    def list(self, request):
        queryset = Officer.objects.all()
        serializer = OfficerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        
        queryset = Officer.objects.filter(user_id = request.user.id)
        # user = get_object_or_404(queryset, pk=pk)
        serializer = OfficerSerializer(queryset,many = True)
        return Response(serializer.data)
    # def has_object_permission(self, request, view, obj):
    #     if request.method in permissions.SAFE_METHODS:
    #         # Allow read-only methods (GET, HEAD, OPTIONS)
    #         return True
    #     # Check if the user is trying to access their own profile when performing other actions
    #     return obj.user_id == request.user_id

    
    # def get_permissions(self):
    #     if self.action == 'list':
    #         # Allow read-only access for list action
    #         return [permissions.IsAuthenticated()]
    #     elif self.action == 'get':
    #         return [permissions.IsAuthenticatedOrReadOnly()]
    #     else:
    #         pass
    #     return super().get_permissions()
officer_list = OfficerProfileViewSet.as_view({'get':'list'})
officer_detail = OfficerProfileViewSet.as_view({'get':'retrieve'})


