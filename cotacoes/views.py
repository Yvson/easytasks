from django.views.generic.base import TemplateView
from django.http import Http404

from .models import Currency, Cryptocurrency


class CurrenciesTemplateView(TemplateView):
    template_name = 'cotacoes/currencies.html'
    view = None

    def dispatch(self, request, reference, *args, **kwargs):
        self.view = reference
        self.currencies_codes = self.get_currencies_codes()
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if not self.view in self.currencies_codes:
            raise Http404("Essa página não existe.")
        self.currencies = self.get_currency(self.view)
        self.currency_references = self.get_currency_references()
        return super().get(request, *args, **kwargs)

    def get_currency(self, code):
        query = Currency.objects.filter(to_currency_code=code).order_by('-date')
        last_update_minute = query[0].date.minute
        next_to_last_update_minute = (last_update_minute - 1) if last_update_minute != 0 else 59
        currencies = query.filter(date__minute=next_to_last_update_minute).order_by('from_country_region')
        return currencies

    def get_currencies_codes(self):
        codes = list(Currency.objects.all().values_list('to_currency_code', flat=True).distinct())
        return codes

    def get_currency_references(self):
        refs = list(Currency.objects.order_by('to_currency_code').values_list('to_currency_code', 'to_country_region').distinct())
        references = [list(f) for f in refs]
        return references
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'cotacoes'
        context["section"] = 'currencies'
        context["currency_set"] = self.currencies
        context["options_currency"] = self.currency_references
        context["current_currency"] = self.view
        context["source_currency"] = self.currencies[0].source
        context["date_currency"] = self.currencies[0].date

        return context


class CryptoCurrenciesTemplateView(TemplateView):
    template_name = 'cotacoes/criptocurrencies.html'
    view = None
    
    def dispatch(self, request, reference, *args, **kwargs):
        self.view = reference
        self.crypto_codes = self.get_cryptocurrency_codes()
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if not self.view in self.crypto_codes:
            raise Http404("Essa página não existe.")
        self.cryptos = self.get_cryptocurrency(self.view)
        self.cryptocurrency_references = self.get_cryptocurrency_references()
        return super().get(request, *args, **kwargs)

    def sort_market_cap(self, element):
        return -float(element.market_cap)

    def get_cryptocurrency(self, code):
        query = Cryptocurrency.objects.filter(to_currency_code=code).order_by('-date', '-market_cap')
        last_update_minute = query[0].date.minute
        next_to_last_update_minute = (last_update_minute - 1) if last_update_minute != 0 else 59
        crypto = list(query.filter(date__minute=next_to_last_update_minute))
        crypto.sort(key=self.sort_market_cap)
        return crypto

    def get_cryptocurrency_codes(self):
        codes = list(Cryptocurrency.objects.order_by('date').values_list('to_currency_code', flat=True).distinct())
        return codes

    def get_cryptocurrency_references(self):
        refs = list(Cryptocurrency.objects.order_by('to_currency_code').values_list('to_currency_code', 'to_country_region').distinct())
        references = [list(f) for f in refs]
        return references

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = 'cotacoes'
        context["section"] = 'criptocurrencies'
        context["currency_set"] = self.cryptos
        context["options_currency"] = self.cryptocurrency_references
        context["current_currency"] = self.view
        context["source_cryptocurrency"] = self.cryptos[0].source
        context["date_cryptocurrency"] = self.cryptos[0].date
        return context

