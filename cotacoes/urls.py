from django.urls import path, include
from .views import CryptoCurrenciesTemplateView, CurrenciesTemplateView



urlpatterns = [
    path('moedas/<str:reference>/', CurrenciesTemplateView.as_view(), name='currencies_view'),
    path('criptomoedas/<str:reference>/', CryptoCurrenciesTemplateView.as_view(), name='cryptocurrencies_view'),
    path('api/', include('cotacoes.api.urls', namespace='api'))
]
