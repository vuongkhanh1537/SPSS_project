from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .user.views import UserView
from .auth.views import LoginViewSet, RegistrationViewSet, RefreshViewSet


router = routers.DefaultRouter()

router.register(r'users', UserView,'user')

# router.register(r'auth',ObtainAuthToken,'auth')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/register', RegistrationViewSet, basename='auth-register')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# router.register(r'token/', TokenObtainPairView.as_view(), basename='token_obtain_pair')
# router.register(r'token/refresh/', TokenRefreshView.as_view(), basename='token_refresh'),
# router.register(r'token/verify/', TokenVerifyView.as_view(), basename='token_verify'),