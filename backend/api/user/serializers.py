from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','username','email','is_active']
        read_only_fields = ['is_active']
        