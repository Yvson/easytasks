from django.core.management.base import BaseCommand
from cotacoes.models import Cryptocurrency

from requests import ConnectionError
from pycoingecko import CoinGeckoAPI
from django.utils.timezone import now
from datetime import timedelta

# Basic Info
currency_info = [
        {'code': 'USD', 'country_region': 'Estados Unidos'},
        {'code': 'EUR', 'country_region': 'União Europeia'},
        {'code': 'BRL', 'country_region': 'Brasil'}
    ]

# CoinGecko Instance
cg = CoinGeckoAPI()


# Command
class Command(BaseCommand):
    help = 'Update the data of cryptocurrency'

    def handle(self, *args, **options):
        try:
            date_now = now()
            crypto_usd = cg.get_coins_markets(vs_currency='USD')
            crypto_brl = cg.get_coins_markets(vs_currency='BRL')
            crypto_eur = cg.get_coins_markets(vs_currency='EUR')

            if (crypto_brl and crypto_usd and crypto_eur):
                
                for crypto_item in crypto_usd:
                    cryptocurrencies_usd = Cryptocurrency(
                        date=date_now,
                        name=crypto_item['name'],
                        symbol=crypto_item['symbol'],
                        to_country_region=currency_info[0]['country_region'],
                        to_currency_code=currency_info[0]['code'],
                        market_cap=crypto_item['market_cap'],
                        circulating_supply=crypto_item['circulating_supply'],
                        max_supply=crypto_item['max_supply'],
                        value=crypto_item['current_price'],
                        source='CoinGecko'
                    )
                    cryptocurrencies_usd.save()
                

                for crypto_item in crypto_eur:
                    cryptocurrencies_eur = Cryptocurrency(
                        date=date_now,
                        name=crypto_item['name'],
                        symbol=crypto_item['symbol'],
                        to_country_region=currency_info[1]['country_region'],
                        to_currency_code=currency_info[1]['code'],
                        market_cap=crypto_item['market_cap'],
                        circulating_supply=crypto_item['circulating_supply'],
                        max_supply=crypto_item['max_supply'],
                        value=crypto_item['current_price'],
                        source='CoinGecko'
                    )
                    cryptocurrencies_eur.save()

                for crypto_item in crypto_brl:
                    cryptocurrencies_brl = Cryptocurrency(
                        date=date_now,
                        name=crypto_item['name'],
                        symbol=crypto_item['symbol'],
                        to_country_region=currency_info[2]['country_region'],
                        to_currency_code=currency_info[2]['code'],
                        market_cap=crypto_item['market_cap'],
                        circulating_supply=crypto_item['circulating_supply'],
                        max_supply=crypto_item['max_supply'],
                        value=crypto_item['current_price'],
                        source='CoinGecko'
                    )
                    cryptocurrencies_brl.save()
                cryptocurrencies = Cryptocurrency.objects.filter(date__lte=now()-timedelta(minutes=5))
                cryptocurrencies.delete()

                self.stdout.write(self.style.SUCCESS('Cryptocurrency data updated.'))

        except ConnectionError:
            self.stdout.write(self.style.ERROR('Cryptocurrency data update failed. Response code: {response.status_code}'))
