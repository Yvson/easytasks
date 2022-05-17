from django.apps import apps
from django.core import serializers
from django.views.generic.base import TemplateView
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .models import Conversion
from .forms import ConversionForm

from ast import literal_eval


# Create your views here.
class ConversorTemplateView(TemplateView):
    model = None
    view = None
    template_name = 'conversor/conversor.html'

    def get_model(self, view_name):
        models = {
            'massa': 'Mass',
            'tempo': 'Time',
            'comprimento': 'Length',
            'area': 'Area',
            'volume': 'Volume',
            'velocidade': 'Velocity',
            'aceleracao': 'Acceleration',
            'forca': 'Force',
            'pressao': 'Pressure',
            'temperatura': 'Temperature',
        }
        return models[view_name]

    def dispatch(self, request, view_name, *args, **kwargs):
        self.model = self.get_model(view_name)
        self.view = view_name
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if (self.request.user.is_authenticated):
            context['saved_conversions'] = Conversion.objects.filter(
                profile=self.request.user.profile)

        current_model = apps.get_model(
            app_label='conversor', model_name=self.model)
        options = current_model.objects.values_list('unit', flat=True)
        fields = [f.name for f in current_model._meta.fields]
        fields.remove('unit')
        measurements = serializers.serialize(
            "json", current_model.objects.all().order_by('pk'), fields=fields)

        context['page'] = 'conversor'
        context['section'] = self.view
        context['options'] = options
        context['measurements'] = measurements

        return context

    @method_decorator(login_required)
    def post(self, request):
        req = literal_eval(request.POST.get('json'))
        data = {
            'profile': self.request.user.profile,
            'unit_from': req['unitfrom'],
            'unit_to': req['unitto'],
        }
        savedConversion_form = ConversionForm(data=data)

        if savedConversion_form.is_valid():
            clean_savedConversion = savedConversion_form.clean()
            try:
                new_savedConversions = Conversion(
                    profile=clean_savedConversion['profile'],
                    unit_from=clean_savedConversion['unit_from'],
                    unit_to=clean_savedConversion['unit_to']
                )
                try:
                    new_savedConversions.save()
                except ValidationError:
                    return JsonResponse({'status': 'Exceeded Limit.'})
                return JsonResponse({'status': 'ok.'})
            except:
                return JsonResponse({'status': 'Exception error.'})
        return JsonResponse({'status': 'Request error.'})

    @method_decorator(login_required)
    def delete(self, request):
        req = literal_eval(request.body.decode('utf-8'))
        conversion_id = str(req['conversionId'])
        if conversion_id:
            try:
                Conversion.objects.filter(
                    profile=self.request.user.profile,
                    id=conversion_id).delete()
                return JsonResponse({'status': 'ok.'})
            except:
                return JsonResponse({'status': 'Exception error.'})
        return JsonResponse({'status': 'Request error.'})
