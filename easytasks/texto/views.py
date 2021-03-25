from django.shortcuts import render
from datetime import datetime

# Create your views here.
def texto_view(request):
    template_name = 'texto/texto.html'

    now = datetime.now()
    
    context = {
        'now': now,
    }

    return render(request, template_name, context)
