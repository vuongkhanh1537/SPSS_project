from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import Group

from api.auth.models import Person, User

class Major(models.IntegerChoices):
    CSE = 1, "Khoa học và kỹ thuật máy tính"
    QLCN = 2, "Quản lý công nghiệp"
    
class Student(Person):
    studentID= models.CharField(max_length=10, null = False)
    major = models.IntegerField(choices= Major.choices,default = Major.CSE)
    pages_remaining =  models.PositiveIntegerField(default = 100)
    class Meta(Person.Meta):
        db_table = "student_info"
    def save(self, *args, **kwargs):
        if not self.pk:  # Only create the user if it doesn't exist
            user = User.objects.create_student(self)
            student_group, _ = Group.objects.get_or_create(name='student')
            user.groups.add(student_group)
            self.user_id = user
            super().save(*args, **kwargs)
class Officer(Person):
    officerID = models.CharField(max_length=10,unique= True, null = False)
    position = models.CharField(max_length=30, default="Officer")
    class Meta(Person.Meta):
        db_table = "officier_info"
    def save(self, *args, **kwargs):
        if not self.pk:  # Only create the user if it doesn't exist
            user = User.objects.create_officer(self)
            student_group, _ = Group.objects.get_or_create(name='pm')
            user.groups.add(student_group)
            self.user_id = user
            super().save(*args, **kwargs)