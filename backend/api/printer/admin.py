from django.contrib import admin

from .models import *

# class Feature(admin.TabularInline):
#     model = Feature
# class ModelPrinterAdmin(admin.ModelAdmin):
#     inlines = [Feature]
#     list_display = ['__str__', 'owner']
#     class Meta:
#         model = ModelPrinter
# admin.site.register(ModelPrinter, ModelPrinterAdmin)
# # class InstitutionAdmin(admin.TabularInline):
# #     model = Institution
# # class BuildingAdmin(admin.TabularInline):
# #     model = Building

# class FloorAdmin(admin.TabularInline):
#     model = Floor

# class PrinterAdmin(admin.ModelAdmin):
#     inlines = [FloorAdmin]
#     list_display = ['__str__', 'owner']
#     class Meta:
#         model = Printer

# admin.site.register(Building)
# admin.site.register(Printer, PrinterAdmin)