from django.db import models


class Currency(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=40)
    date = models.DateTimeField()
    from_country_region = models.CharField(max_length=40)
    to_country_region = models.CharField(max_length=40)
    from_currency_code = models.CharField(max_length=15)
    to_currency_code = models.CharField(max_length=15)
    value = models.DecimalField(max_digits=20, decimal_places=4)
    source = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'
        ordering = ["from_country_region"]

    def __str__(self):
        return f'{self.name}'

    
class Cryptocurrency(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=40)
    symbol = models.CharField(max_length=10)
    date = models.DateTimeField()
    to_currency_code = models.CharField(max_length=15)
    to_country_region = models.CharField(max_length=30)
    market_cap = models.DecimalField(max_digits=20, decimal_places=4)
    circulating_supply = models.BigIntegerField(blank=True, null=True)
    max_supply = models.BigIntegerField(blank=True, null=True)
    value = models.DecimalField(max_digits=20, decimal_places=4)
    source = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Cryptocurrency'
        verbose_name_plural = 'Cryptocurrencies'
        ordering = ["-market_cap"]

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def get_last_n(n):
        return Cryptocurrency.objects.all()[0:n]

