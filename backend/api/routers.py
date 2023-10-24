from rest_framework import routers

from .user.views import UserView
from .auth.views import LoginViewSet, RegistrationViewSet, RefreshViewSet


router = routers.DefaultRouter()

router.register(r'users', UserView,'user')

router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/register', RegistrationViewSet, basename='auth-register')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
