from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','username','first_name','last_name','email', 'phone','is_active','is_staff']
        read_only_fields = ['major','is_active',
                            'is_staff']
        