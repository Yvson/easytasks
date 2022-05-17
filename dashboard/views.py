from django.shortcuts import render
from django.views.generic.base import TemplateView

from cotacoes.models import Currency, Cryptocurrency



class DashboardTemplateView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    currency_list = ['USD', 'EUR', 'ARS', 'CNY', 'CAD', 'GBP', 'CLP']
    cryptocurrency_list = ['btc', 'eth', 'zec', 'ltc', 'bnb', 'ada', 'dot']

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_currency_list(self):
        currency_list = Currency.objects.filter(to_currency_code='BRL', from_currency_code__in=self.currency_list)
        return currency_list

    def get_cryptocurrency_list(self):
        cryptocurrency_list = Cryptocurrency.objects.filter(to_currency_code='BRL', symbol__in=self.cryptocurrency_list)
        return cryptocurrency_list
    
    def get_last_currency(self):
        last_currency = Currency.objects.latest('pk')
        return last_currency

    def get_last_cryptocurrency(self):
        last_cryptocurrency = Cryptocurrency.objects.latest('pk')
        return last_cryptocurrency

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'dashboard'
        #context["currency_list"] = self.get_currency_list()
        #context["cryptocurrency_list"] = self.get_cryptocurrency_list()
        #context["last_update"] = self.get_last_currency().date
        #context["currency_source"] = self.get_last_currency().source
        #context["cryptocurrency_source"] = self.get_last_cryptocurrency().source

        return context
    

def notfound_view(request, exception):
    template_name = 'dashboard/404.html'

    return render(request, template_name, status=404)
