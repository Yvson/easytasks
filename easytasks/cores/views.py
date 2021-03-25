from django.shortcuts import render

# Create your views here.
def cores_view(request):
    template_view = 'cores/cores.html'

    context = {
        'test': 'cores'
    }

    return render(request, template_view, context)