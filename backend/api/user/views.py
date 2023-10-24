from django.shortcuts import render
from .models import User
from .serializers import UserSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
# Create your views here.

class UserView(viewsets.ModelViewSet):
    http_method_names=['get']
    serializer_class=UserSerializer
    permission_classes= (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated']
    ordering = ['-updated']
    
    def get_queryset(self):
        if self.request.user_is_superuser:
            return User.objects.all()
    def get_object(self):
        lookup_field_value= self.kwargs[self.lookup_field] #return id
        obj = User.objects.get(lookup_field_value)
        self.check_object_permissions(self.request , obj)
