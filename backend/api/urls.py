from django.contrib import admin
from django.urls import path, include

from routers import router
urlpatterns = [
    path('api/', include((router.urls, 'userlist'), namespace='userlist')),
]
