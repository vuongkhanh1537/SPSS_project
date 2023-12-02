import uuid
from django.db import models
from django.conf import settings
from api.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from compositefk.fields import CompositeForeignKey
# from viewflow.fields import CompositeKey
from collections import OrderedDict
from mptt.models import MPTTModel, TreeForeignKey

class ObjectTracking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,related_name='created_by')
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,null = True, on_delete=models.DO_NOTHING, related_name='modified_by')
    class Meta:
        abstract = True
        ordering = ('-created_at',)

class ModelPrinterManager(models.Manager):
    def all_objects(self):
        return super().get_queryset()

class ModelPrinter(models.Model):
    model = models.CharField(max_length=12,null=False, blank=False)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING,related_name='model_created_by')
    modified_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, related_name='model_modified_by')
    objects = ModelPrinterManager()

    def __str__(self):
        return self.model

    @property
    def features(self):
        return self.feature_set.all()

class FeatureChoices(models.TextChoices):
    SCAN = "Scan"
    PRINT = "Print"
    Photocopy = "Photocopy"
    
class Feature(models.Model):
    model = models.ForeignKey('ModelPrinter', on_delete=models.CASCADE)
    feature = models.CharField(max_length=10, choices= FeatureChoices.choices,null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class PrinterManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=1)

    def all_objects(self):
        return super().get_queryset()

    def inactive(self):
        return self.all_objects().filter(status=2)

class Institution(models.IntegerChoices):
    CS1 = 1 , 'Cơ sở 1'
    CS2 = 2, 'Cơ sở 2'

class Floor(models.Model):
    building_code = models.ForeignKey("Building", on_delete=models.CASCADE)
    floor_code = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.building_code} - Tầng {self.floor_code}"
    
class Building(models.Model):
    inst = models.IntegerField(choices=Institution.choices, default = Institution.CS1, null = False)
    building = models.CharField(max_length=2)
    # building_of_institution = CompositeKey(columns =['inst','building'])
    
    def __str__(self):
        return f"Cơ sở {self.inst} - Tòa {self.building}"
    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)
        if self.inst == 2:
            for floor in range(8):
                bldg = Floor(floor_code=floor, building_code=self)
                bldg.save()
        else:
            for floor in range(5):
                bldg = Floor(floor_code=floor, building_code=self)
                bldg.save()
class PrinterStatus(models.IntegerChoices):
    ACTIVE = 1,'Active'
    OFFLINE = 3, 'Offline'
    ERROR = 4, 'Error'
    BUSY = 5, 'Busy'
    MAINTAINANCE=2, 'Maintenance'
    
class Printer(ObjectTracking):
    # uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    model = models.ForeignKey("ModelPrinter",  on_delete=models.CASCADE)       
    floor = models.ForeignKey(
        Floor, related_name="printer_floor", on_delete=models.CASCADE
    )
    pages_remaining = models.PositiveIntegerField()
    ink_status = models.BooleanField(default = True)
    status = models.IntegerField(choices = PrinterStatus.choices, default= PrinterStatus.ACTIVE)
    objects = PrinterManager()
    
    # Add a field to store the floor description
    floor_description = models.CharField(max_length=255, blank=True, null=True)
    # def get_tongthoigian(self, orderprinter):
    #     oder_printer.objects.filter(printer = printer_id, is_printed = false)
    #     return sum(mayorde)
    def save(self, *args, **kwargs):
        # Get the floor description from the related Floor object
        if self.floor:
            floor_description = f"{self.floor.building_code} - Tầng {self.floor.floor_code}"
            self.floor_description = floor_description
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.model} - {self.floor_description}"
class OrderPrinter(models.Model):
    printer = models.ForeignKey('Printer', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    file_upload = models.FileField( upload_to='local/')
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_printed = models.BooleanField(default=False)
    print_date = models.DateTimeField(null=True, blank=True)
    is_cancelled = models.BooleanField(default=False)
    # @property
    # def get_time(self):
    #     pass khi maf thang user kia xong thi thang nay moi tru
    file_name = models.CharField( max_length=50)
    pages =  models.PositiveIntegerField()
    
    # @property
    def get_time(self):
        return str(self.pages*2)
    
    # def get_pdf_page_count(path):
    #     with open(path, 'rb') as fl:
    #         reader = PdfFileReader(fl)
    #     return reader.getNumPages()
    
    