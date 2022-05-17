from django.urls import path
from . import views


urlpatterns = [
    path('<str:text_view>', views.TextTemplateView.as_view(), name='texto_view'),
]
