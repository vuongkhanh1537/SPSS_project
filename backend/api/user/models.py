from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone

class UserManager(UserManager):
    def _create_user(self,username,first_name,last_name, email, password,phone, **extra_fields):
        """Create and return a `User` with an email, phone number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        
        user = self.model(username= username,first_name=first_name, last_name=last_name,email=self.normalize_email(email),phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
    
        return user
    
    def create_user(self,username = None,first_name= None, last_name=None, email=None, password=None,phone=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(username,first_name,last_name,email, password,phone, **extra_fields)
    
    def create_superuser(self,username=None,first_name= None, last_name=None, email=None,phone=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self._create_user(username,first_name,last_name,email, password,phone, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    Major = [
        ("CSE", "Khoa học và kĩ thuật máy tính"),
        ("SO", "Sophomore"),
        ("JR", "Junior"),
        ("SR", "Senior"),
        ("GR", "Graduate"),
    ]
    first_name= models.CharField(max_length=10,null=False)
    last_name=models.CharField(max_length=10,null=False)
    username = models.CharField(db_index=True, max_length=255, unique=True, null= True, blank = True)
    email = models.EmailField(db_index=True, unique=True,  null=True, blank=True)
    phone = models.CharField(max_length=10,null=False)
    major = models.CharField(choices= Major,default = "CSE", max_length=50)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    #last_login = models.DateTimeField(_("last login"), blank=True, null=True)
    
    USERNAME_FIELD = 'username' #is a string that specifies the name of the field on the user model that is used as the username.
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','email', 'phone'] #is a list of the names of the fields that will be prompted for when creating a 
                                #user via the createsuperuser management command. Here, it includes 'username', 
                                #which means when a superuser is created, they will be prompted to provide a username.
                                # ['mssv', 'major',....]


    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.first_name +' '+ self.last_name
    def __str__(self):
        return self.username
    # def get_short_name(self):
    #     return self.usernamename or self.email.split('@')[0]