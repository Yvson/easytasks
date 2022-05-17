from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('<str:view_name>/', views.ConversorTemplateView.as_view(),
         name="conversor_view"),
]
