from django.urls import include, path
from rest_framework import routers
from . import views



urlpatterns = [
    path('bycountry/', views.SubCountiesView),
    path('nearest/', views.get_nearest_facilities),
   
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]




from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)