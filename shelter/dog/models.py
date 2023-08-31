from django.db import models
from django.contrib.gis.db import models

class dogShelter(models.Model):
    geom = models.PointField(blank=True, null=True)
    img = models.ImageField(upload_to='images/',blank=True, null=True)
    addr_city = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_street = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    name = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.

   

class SubCounties(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    constituen = models.CharField(max_length=50, blank=True, null=True)
