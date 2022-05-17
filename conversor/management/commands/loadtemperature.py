from django.core.management.base import BaseCommand
from conversor.models import Temperature


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        file = open(kwargs['path'], 'r')
        temperature = []
        for temperature_object in file:
            temperature.append(temperature_object)

        for temperature_object in temperature:
            temperature_filter = temperature_object.rstrip().split(',')
            temperature_item = Temperature(
                unit=temperature_filter[0],
                celsius=temperature_filter[1],
                delisle=temperature_filter[2],
                fahrenheit=temperature_filter[3],
                kelvin=temperature_filter[4],
                newton=temperature_filter[5],
                rankine=temperature_filter[6],
                reaumur=temperature_filter[7],
                romer=temperature_filter[8],
            )
            temperature_item.save()
        self.stdout.write(self.style.SUCCESS(
            'Temperature data loaded to database.'))
