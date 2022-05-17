from django.urls import path
from .views import CookieView





urlpatterns = [
    path('', CookieView.as_view(), name='cookie_view')
]
