from django.shortcuts import render
from datetime import datetime

# Create your views here.
def gerador_numbers_view(request):
    template_name = 'gerador/numbers.html'
    now = datetime.now()
    
    context = {
        'now': now,
    }

    return render(request, template_name, context)

def gerador_passwords_view(request):
    template_name = 'gerador/passwords.html'
    now = datetime.now()
    
    context = {
        'now': now,
    }

    return render(request, template_name, context)