from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('numeros/', views.NumbersTemplateView.as_view(), name="numbers_view"),
    path('numeros/<str:number_id>/',
         views.NumbersTemplateView.as_view(), name="number_view"),
    path('senhas/', views.PasswordsTemplateView.as_view(), name="passwords_view"),
]
