from django.db import models
from django.contrib.auth.models import  BaseUserManager, AbstractBaseUser, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True, null= True, blank = True)
    email = models.EmailField(db_index=True, unique=True,  null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    #last_login = models.DateTimeField(_("last login"), blank=True, null=True)
    
    USERNAME_FIELD = 'username' #is a string that specifies the name of the field on the user model that is used as the username.
    REQUIRED_FIELDS = ['email'] #is a list of the names of the fields that will be prompted for when creating a 
                                #user via the createsuperuser management command. Here, it includes 'username', 
                                #which means when a superuser is created, they will be prompted to provide a username.
                                # ['mssv', 'major',....]

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
    
