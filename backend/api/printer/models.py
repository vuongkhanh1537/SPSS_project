from django.db import models
from api.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from compositefk.fields import CompositeForeignKey
from viewflow.fields import CompositeKey
from collections import OrderedDict

class ObjectTracking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

class ModelPrinterManager(models.Manager):
    def all_objects(self):
        return super().get_queryset()

class ModelPrinter(ObjectTracking):
    model = models.CharField(max_length=12,null=False, blank=False)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    
    objects = ModelPrinterManager()

    def __str__(self):
        return self.model

    @property
    def features(self):
        return self.feature_set.all()


class Feature(models.Model):
    model = models.ForeignKey('ModelPrinter', on_delete=models.CASCADE)
    feature = models.CharField(max_length=10,null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class PrinterManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=1)

    def all_objects(self):
        return super().get_queryset()

    def inactive(self):
        return self.all_objects().filter(status=2)
class Institution(models.Model):
    code = models.CharField(max_length=3, primary_key= True) #cs1 cs2
    name= models.CharField(max_length = 7)
    
    def __str__(self):
        return self.code

class Building(models.Model):
    inst = models.ForeignKey("Institution", on_delete=models.CASCADE)
    building = models.CharField(max_length=2)
    # building_of_institution = CompositeKey(columns =['inst','building'])
    
    # def __str__(self):
    #     return self.inst + self.building

class Floor(models.Model):
    inst_code = models.CharField(max_length=3)
    building_code = models.CharField(max_length=2)
    building = CompositeForeignKey(Building,related_query_name="floors",on_delete = models.CASCADE,
                                   to_fields=OrderedDict([
                                       ('inst','inst_code'),
                                       ('building','building_code'),
                                   ]))
    floor= models.PositiveIntegerField()
class PrinterStatus(models.IntegerChoices):
    ACTIVE = 1,'Active'
    OFFLINE = 3, 'Offline'
    ERROR = 4, 'Error'
    BUSY = 5, 'Busy'
    MAINTAINANCE=2, 'Maintenance'
    
class Printer(ObjectTracking):
    model = models.ForeignKey("ModelPrinter",  on_delete=models.CASCADE)       
    inst_code = models.CharField(max_length=3)
    building_code =  models.CharField(max_length=2)
    floor_code = models.PositiveIntegerField()
    
    floor = CompositeForeignKey(Floor,related_query_name="printers",on_delete = models.CASCADE,
                                   to_fields=OrderedDict([
                                       ('inst_code','inst_code'),
                                       ('building_code','building_code'),
                                       ('floor','floor_code'),
                                   ]))
    
    status = models.IntegerField(choices = PrinterStatus.choices, default= PrinterStatus.ACTIVE)
    objects = PrinterManager()
    


