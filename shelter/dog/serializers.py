from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import  SubCounties,dogShelter

class SubCountiesSerializer(GeoFeatureModelSerializer):

	class Meta:
		model = SubCounties
		fields = '__all__'
		geo_field = 'geom'

    
class dogShelterSerializer(GeoFeatureModelSerializer):
    	
	distance = serializers.CharField()

	class Meta:
		model = dogShelter
		fields = '__all__'
		geo_field = 'geom'
		# read_only_fields = ['distance']