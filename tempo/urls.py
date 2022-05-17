from django.urls import path
from . import views

urlpatterns = [
    path('relogio/', views.RelogioTemplateView.as_view(), name="time_view"),
    path('cronometro/', views.CronometroTemplateView.as_view(),
         name="stopwatch_view"),
    path('temporizador/', views.TemporizadorTemplateView.as_view(), name="timer_view"),
]
