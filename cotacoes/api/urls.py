from django.urls import path
from . import views

app_name = 'cotacoes'

urlpatterns = [
    path('moedas/', views.CurrencyListView.as_view(), name='currencies_list'),
    path('criptomoedas/', views.CryptocurrencyListView.as_view(), name='cryptocurrencies_list')
]
