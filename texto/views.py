from django.views.generic.base import TemplateView
from django.http import Http404


class TextTemplateView(TemplateView):
    template_name = 'texto/texto.html'
    view = None
    view_options = [
        'letras_maiusculas',
        'letras_minusculas',
        'primeira_letra_maiuscula',
        'maiusculas_minusculas',
        'binario',
        'inverter'
    ]

    def dispatch(self, request, text_view, *args, **kwargs):
        self.view = text_view
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'texto'
        context["section"] = self.view
        return context

    def get(self, request, *args, **kwargs):
        if not self.view in self.view_options:
            raise Http404("Essa página não existe.")
        return super().get(request, *args, **kwargs)
