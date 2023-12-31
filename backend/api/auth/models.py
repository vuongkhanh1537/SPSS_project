from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.contrib.auth.models import Group
from django.utils import timezone
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from rest_framework import reverse
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserManager(UserManager):
    
    def _create_user(self,username, email, password, **extra_fields):
        """Create and return a `User` with an email, phone number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        
        user = self.model(username= username,email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
    
        return user
    
    def create_user(self,username = None,  email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(username,email, password, **extra_fields)
    def create_staff(self,username = None,  email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(username,email, password, **extra_fields)
    def create_superuser(self,username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self._create_user(username,email, password, **extra_fields)
    
    def create_student(self, student):

        username = f"{student.first_name}.{student.last_name}{student.studentID}"
        password = "12345678"
        email = f"{username}@hcmut.edu.vn"
        return self.create_user(username=username, password=password, email=email)
        # student.user_id = user  # Associate the student with the user

        # Attach the student to the 'student' group
        # student_group, _ = Group.objects.get_or_create(name='student')
        # user.groups.add(student_group)

    def create_officer(self, officer):

        username = f"{officer.first_name}.{officer.last_name}{officer.officerID}"
        password = "12345678"
        email = f"{username}@hcmut.edu.vn"
        return self.create_staff(username=username, password=password, email=email)
        #officer.user_id = user  # Associate the officer with the user

        # Attach the officer to the 'pm' group
        # pm_group, _ = Group.objects.get_or_create(name='pm')
        # user.groups.add(pm_group)
class User(AbstractBaseUser, PermissionsMixin):
    
    id= models.AutoField(primary_key=True)
    username = models.CharField(db_index=True, max_length=30, unique=True, null= True, blank = True)
    email = models.EmailField(db_index=True, unique=True,  null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    #last_login = models.DateTimeField(_("last login"), blank=True, null=True)
    
    USERNAME_FIELD = 'username' #is a string that specifies the name of the field on the user model that is used as the username.
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email'] 

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
# # Create your models here.
class Person(models.Model):
    user_id = models.OneToOneField(User,parent_link=True,primary_key=True, on_delete=models.CASCADE)
    first_name= models.CharField(max_length=10,null=False)
    last_name=models.CharField(max_length=10,null=False)
    phone = models.CharField(max_length=10,null=False)
    
    def get_full_name(self):
        return self.first_name +' '+ self.last_name
    
    class Meta:
        abstract = True
        ordering = ['user_id']
        
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
