from django.urls import path
from . import views

# app_name ='cores'

urlpatterns = [
    path('', views.cores_view, name="cores_view"),
]


