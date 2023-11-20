from django.contrib import admin

from .auth.models import User
from .user.models import Student,Officer
from .printer.models import *

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Officer)


admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Printer)
admin.site.register(ModelPrinter)
admin.site.register(Feature)
admin.site.register(OrderPrinter)