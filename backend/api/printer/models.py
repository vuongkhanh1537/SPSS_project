from django.db import models
from api.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey


class ObjectTracking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

class ModelPrinterManager(models.Manager):
    # def get_queryset(self):
    #     return super().get_queryset().filter(status="active")

    def all_objects(self):
        return super().get_queryset()

    # def inactive(self):
    #     return self.all_objects().filter(status='inactive')



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

    def __str__(self):
        return self.text



