from django.urls import path
from . import views


urlpatterns = [
    path('', views.texto_view, name='texto_view'),
]
