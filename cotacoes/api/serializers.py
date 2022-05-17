from rest_framework import serializers
from ..models import Currency, Cryptocurrency




class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = [
            'date',
            'from_country_region',
            'name',
            'from_currency_code',
            'to_currency_code',
            'value',
            'source'
        ]
            
class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = [
            'date',
            'name',
            'symbol',
            'to_currency_code',
            'value',
            'source'
        ]
