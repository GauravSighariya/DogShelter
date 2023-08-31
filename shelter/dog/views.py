from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry,Point
from rest_framework.decorators import action
from django_filters import rest_framework  as filters
from . hospital_filters import NairobiHealthFacilitiesFilter
from . models import  SubCounties,dogShelter
from . serializers import  SubCountiesSerializer, dogShelterSerializer


    
@api_view(['GET'])
def SubCountiesView(request):
    queryset = SubCounties.objects.all()
    serializer = SubCountiesSerializer(queryset,many=True)
    return Response(serializer.data)



@api_view(['GET'])
def get_nearest_facilities(request):
    x_coords = request.GET.get('latitude', None)
    y_coords = request.GET.get('longitude', None)
    
    if x_coords and y_coords:
        user_location = Point(float(x_coords), float(y_coords), srid=4326)
        nearest_five_facilities = dogShelter.objects.annotate(distance=Distance('geom', user_location)).order_by('distance')[:5]
        
        serializer = dogShelterSerializer(nearest_five_facilities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)