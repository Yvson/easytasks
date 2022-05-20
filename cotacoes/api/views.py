from rest_framework import generics
from ..models import Currency, Cryptocurrency
from .serializers import CurrencySerializer, CryptocurrencySerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


currency_list = ['USD', 'EUR', 'ARS', 'CNY', 'CAD', 'GBP', 'CLP']
cryptocurrency_list = ['btc', 'eth', 'zec', 'ltc', 'bnb', 'ada', 'dot']

class CurrencyListView(generics.ListAPIView):
    serializer_class = CurrencySerializer

    @method_decorator(cache_page(60*2))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        query = Currency.objects.filter(to_currency_code='BRL', from_currency_code__in=currency_list).order_by('-date')
        last_update_minute = query[0].date.minute
        next_to_last_update_minute = (last_update_minute - 1) if last_update_minute != 0 else 59
        currencies = query.filter(date__minute=next_to_last_update_minute).order_by('from_country_region')
        return currencies



class CryptocurrencyListView(generics.ListAPIView):
    serializer_class = CryptocurrencySerializer

    @method_decorator(cache_page(60*2))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        query = Cryptocurrency.objects.filter(to_currency_code='BRL', symbol__in=cryptocurrency_list).order_by('-date')
        last_update_minute = query[0].date.minute
        next_to_last_update_minute = (last_update_minute - 1) if last_update_minute != 0 else 59
        cryptos = query.filter(date__minute=next_to_last_update_minute).order_by('-market_cap')
        return cryptos

