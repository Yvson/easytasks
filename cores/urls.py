from django.urls import path
from .views import CoresTemplateView

# app_name ='cores'

urlpatterns = [
    path('<str:cores_view>', CoresTemplateView.as_view(), name="cores_view"),
]
