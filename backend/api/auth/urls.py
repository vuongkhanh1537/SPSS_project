from django.urls import path

from .views import  LogoutAndBlacklistRefreshTokenForUserView

urlpatterns = [

    path('blacklist/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist')
]