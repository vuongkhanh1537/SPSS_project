from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from . import views
from api.printer.views import *
from api.auth.views import HelloWorldView
from django.contrib.auth import views as auth_views
# from .views import api_home
router = DefaultRouter()
router.register('model', ModelPrinterViewSet)


model_list_view = ModelPrinterViewSet.as_view({
    "get": "list",
    "post": "create"
})

urlpatterns = [
    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('orders/<pk>/', get_time),
    #printer
    # path('add_model_printer', model_printer_create),
    path('hello/', HelloWorldView.as_view()),
    path('',include(router.urls))
]