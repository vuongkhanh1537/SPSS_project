from django.contrib import admin

from .auth.models import User, Student,Officer
# from .user.models import Student,Officer

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Officer)
