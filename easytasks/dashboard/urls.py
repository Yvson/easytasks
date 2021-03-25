from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.dashboard_view, name="dashboard_view"),
    path('login/', views.login_view, name="login_view"),
    path('registration/', views.registration_view, name="registration_view"),
    path('logout/', views.logout_view, name="logout_view"),
    path('recovery/', views.recovery_view, name="recovery_view"),

]





# if settings.DEBUG:
#      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)