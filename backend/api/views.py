from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
# Create your views here.

# class TodoView(viewsets.ModelViewSet):
#     serializer_class = TodoSerializer
#     def get_queryset(self):
#         return Todo.objects.all()
    