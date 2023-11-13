from django.contrib import admin

from .auth.models import User
from .user.models import Student,Officer

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Officer)
