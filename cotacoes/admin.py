from django.contrib import admin
from .models import Currency, Cryptocurrency




@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name',
                    'date',
                    'from_country_region',
                    'to_country_region',
                    'from_currency_code',
                    'to_currency_code',
                    'value',
                    'source']

@admin.register(Cryptocurrency)
class CriptocurrencyAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name',
                    'symbol',
                    'date',
                    'to_country_region',
                    'to_currency_code',
                    'market_cap',
                    'circulating_supply',
                    'max_supply',
                    'value',
                    'source'
                    ]
                    
                    
                    
                    
                    
                    
                    