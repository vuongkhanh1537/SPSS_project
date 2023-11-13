from rest_framework import serializers
from .models import User
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers
from django.contrib.auth import get_user_model

# User = get_user_model()

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
 
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
            user = User.objects.create_user(**validated_data)
        return user