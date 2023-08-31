from django.contrib import admin
from . models import *
from django.contrib.gis.admin import OSMGeoAdmin
# Register your models here.



class dogShelterAdmin(OSMGeoAdmin):
    default_zoom = 6  # Adjust this value as needed

class SubCountiesAdmin(OSMGeoAdmin):
    default_zoom = 6  # Adjust this value as needed

admin.site.register(dogShelter, dogShelterAdmin)

admin.site.register(SubCounties,SubCountiesAdmin)