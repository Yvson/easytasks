from django.shortcuts import render
from datetime import datetime


# Create your views here.
def dashboard_view(request):
    template_name = 'dashboard/dashboard.html'
    now = datetime.now()
    
    context = {
        'now': now,
    }

    return render(request, template_name, context)

def login_view(request):
    template_name = 'registration/login.html'
    now = datetime.now()
    
    context = {
        'now': now,
    }

    return render(request, template_name, context)

def registration_view(request):
    template_name = 'registration/registration.html'
    now = datetime.now()
    
    context = {
        'now': now,
    }

    return render(request, template_name, context)

def logout_view(request):
    template_name = 'registration/logout.html'
    now = datetime.now()
    
    context = {
        'now': now,
    }

    return render(request, template_name, context)

def recovery_view(request):
    template_name = 'registration/recovery.html'
    now = datetime.now()
    
    context = {
        'now': now,
    }

    return render(request, template_name, context)
