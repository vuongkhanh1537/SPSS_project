from django.urls import include, re_path, path

from rest_framework.authtoken import views
from rest_framework_simplejwt import views as jwt_views
from .views import  CustomUserCreate, HelloWorldView, LogoutAndBlacklistRefreshTokenForUserView

urlpatterns = [
    re_path(r'^api-token-auth/', views.obtain_auth_token),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
