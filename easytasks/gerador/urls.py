from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('numeros/', views.gerador_numbers_view, name="numbers_view"),
    path('senhas/', views.gerador_passwords_view, name="passwords_view"),
]
