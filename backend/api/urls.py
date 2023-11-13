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
# from .views import api_home
router = DefaultRouter()
router.register('model', ModelPrinterViewSet)


model_list_view = ModelPrinterViewSet.as_view({
    "get": "list",
    "post": "create"
})

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('token/obtain', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #printer
    # path('add_model_printer', model_printer_create),
    # path('add_feature', feature_create)
    path('',include(router.urls))
]