"""easytasks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('conversor/', include('conversor.urls')),
    path('gerador/', include('gerador.urls')),
    path('texto/', include('texto.urls')),
    path('cores/', include('cores.urls')),
    path('tempo/', include('tempo.urls')),
    path('cotacoes/', include('cotacoes.urls')),
    path('conta/', include('conta.urls')),
    path('suporte/', include('suporte.urls')),
    path('cookies/', include('cookies.urls')),
]


handler404 = 'dashboard.views.notfound_view'
