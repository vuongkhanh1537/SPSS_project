from rest_framework import serializers
from .models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add your extra responses here
        data['is_staff'] = self.user.is_staff
        # data['groups'] = self.user.groups.values_list('name', flat=True)
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','username','email', 'is_active','is_staff']
        read_only_fields = ['is_active']
 
class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def create(self, validated_data):
        try:
            user = User.objects.get(username=validated_data['username'])
        except ObjectDoesNotExist:
            user = User.objects.create_st(**validated_data)
        return user