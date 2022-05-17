from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import Http404
from django.core import serializers
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import ColorForm
from .models import Color

from ast import literal_eval


class CoresTemplateView(TemplateView):
    template_name = 'cores/cores.html'
    model = Color
    view = None
    view_options = [
        'analogo',
        'monocromatico',
        'triade',
        'complementar',
        'quadrado',
    ]
    colors = None

    def dispatch(self, request, cores_view, *args, **kwargs):
        self.view = cores_view
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if not self.view in self.view_options:
            raise Http404("Essa página não existe.")
        if self.request.user.is_authenticated:
            self.colors = self.get_serialized_colors(
                profile=self.request.user.profile)

        return super().get(request, *args, **kwargs)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        req = literal_eval((request.POST.get('json')))
        data = {
            'profile': self.request.user.profile,
            'color': req['color'],
        }
        savedColor_form = ColorForm(data=data)

        if savedColor_form.is_valid():
            clean_savedColor = savedColor_form.clean()
            try:
                new_savedColor = Color(
                    profile=clean_savedColor['profile'],
                    color=clean_savedColor['color'],
                )
                try:
                    new_savedColor.save()
                except ValidationError:
                    return JsonResponse({'status': 'Exceeded Limit.'})
                return JsonResponse({'status': 'ok.'})
            except:
                return JsonResponse({'status': 'Exception error.'})
        return JsonResponse({'status': 'Request error.'})

    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        req = literal_eval(request.body.decode('utf-8'))
        colors_ids = list(req['colorsIds'])

        if colors_ids:
            try:
                Color.objects.filter(
                    profile=self.request.user.profile,
                    id__in=colors_ids).delete()
                return JsonResponse({'status': 'ok.'})
            except:
                return JsonResponse({'status': 'Exception error.'})
        return JsonResponse({'status': 'Request error.'})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["page"] = 'cores'
        context["section"] = self.view
        context["colors"] = self.colors
        return context

    def get_serialized_colors(self, profile):
        fields = [f.name for f in self.model._meta.fields]
        colors = serializers.serialize(
            "json", self.model.objects.filter(profile=profile).order_by('-date'), fields=fields)
        return colors
