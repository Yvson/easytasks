from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def conversor_mass_view(request):
    template_name = 'conversor/conversor.html'

    now = datetime.now()
    
    context = {
        'now': now,
    }

    return render(request, template_name, context)
