from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt import views as jwt_views

from api.auth.views import  CustomUserCreate, HelloWorldView, LogoutAndBlacklistRefreshTokenForUserView

from . import views
from api.printer.views import *
from api.auth.views import HelloWorldView, MyTokenObtainPairView
from django.contrib.auth import views as auth_views
# from .views import api_home
router = DefaultRouter()
router.register('model', ModelPrinterViewSet)


model_list_view = ModelPrinterViewSet.as_view({
    "get": "list",
    "post": "create"
})
# router.register(r'printers', PrinterViewSet, basename='printer')
urlpatterns = [
    
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/',  MyTokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('blacklist/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),
    #printer
    path('printers/',include('api.printer.urls', namespace = 'printers')),
    path('',include(router.urls))
]