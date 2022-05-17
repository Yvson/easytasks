from django.urls import path
from .views import DashboardTemplateView, notfound_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardTemplateView.as_view(), name="dashboard_view"),
    path('nao-encontrado/', notfound_view, name="notfound_view")
]
