from api.user.models import User
from api.user.serializers import UserSerializer

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer
from rest_framework_simplejwt.settings import api_settings

from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        
        data['user'] = UserSerializer(self.user).data
        data['refresh']=str(refresh)
        data['access']=str(refresh.access_token)
        
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(user= self.user)
        return data
    
class RegisterSerializer(UserSerializer):
    Major = [
        ("CSE", "Khoa học và kĩ thuật máy tính"),
        ("SO", "Sophomore"),
        ("JR", "Junior"),
        ("SR", "Senior"),
        ("GR", "Graduate"),
    ]
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=128)
    username = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    last_name= serializers.CharField(max_length =10,write_only=True, required = True)
    first_name= serializers.CharField(max_length =10,write_only=True, required = True)
    phone= serializers.CharField(max_length =10,write_only=True, required = True)
    major = serializers.ChoiceField(choices=Major, default="CSE")
    class Meta:
        model = User
        fields = ['id', 'username','first_name', 'last_name', 'email','phone', 'password','major', 'is_active','is_staff','is_superuser','date_joined']

    def create(self, validated_data):
        try:
            user = User.objects.get(username=validated_data['username'])
        except ObjectDoesNotExist:
            user = User.objects.create_user(**validated_data)
        return user