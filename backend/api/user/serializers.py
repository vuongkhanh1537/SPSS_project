from rest_framework import serializers

from .models import Student, Officer, Person
from api.auth.serializers import UserSerializer
class PersonSerializer(UserSerializer):

    class Meta:
        model = Person
        fields = ['user_id','first_name', 'last_name', 'phone']
        read_only_fields= ['user_id']
        abstract = True
class StudentSerializer(PersonSerializer):
    class Meta:
        model = Student
        fields = ['user_id','studentID', 'first_name', 'last_name', 'phone','major']
        read_only_fields = ['studentID', 'first_name','last_name','major']
class OfficerSerializer(PersonSerializer):
    class Meta:
        model = Officer
        fields = ['user_id','officerID', 'first_name', 'last_name', 'phone','position']
        read_only_fields = ['officerID', 'position']