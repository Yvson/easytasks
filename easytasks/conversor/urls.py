from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('massa/', views.conversor_mass_view, name="mass_view"),
    path('tempo/', views.conversor_mass_view, name="time_view"),
    path('comprimento/', views.conversor_mass_view, name="length_view"),
    path('area/', views.conversor_mass_view, name="area_view"),
    path('volume/', views.conversor_mass_view, name="volume_view"),
    path('velocidade/', views.conversor_mass_view, name="speed_view"),
    path('aceleracao/', views.conversor_mass_view, name="aceleration_view"),
    path('forca/', views.conversor_mass_view, name="force_view"),
    path('pressao/', views.conversor_mass_view, name="pressure_view"),
    path('temperatura/', views.conversor_mass_view, name="temperature_view"),
]



# if settings.DEBUG:
#      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)