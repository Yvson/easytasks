from django.core.management.base import BaseCommand
from conversor.models import Time

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
    
    def handle(self, *args, **kwargs):
        file = open(kwargs['path'], 'r')
        time = []
        for time_object in file:
            time.append(time_object)

        for time_object in time:
            time_filter = time_object.rstrip().split(',')
            time_item = Time(
                    unit = time_filter[0],
                    ano = time_filter[1],
                    attosegundo = time_filter[2],
                    centisegundo = time_filter[3],
                    decasegundo = time_filter[4],
                    decisegundo = time_filter[5],
                    dia = time_filter[6],
                    exasegundo = time_filter[7],
                    femtosegundo = time_filter[8],
                    gigasegundo = time_filter[9],
                    hectosegundo = time_filter[10],
                    hora = time_filter[11],
                    megasegundo = time_filter[12],
                    mes = time_filter[13],
                    microsegundo = time_filter[14],
                    milisegundo = time_filter[15],
                    minuto = time_filter[16],
                    nanosegundo = time_filter[17],
                    petasegundo = time_filter[18],
                    picosegundo = time_filter[19],
                    quilosegundo = time_filter[20],
                    segundo = time_filter[21],
                    semana = time_filter[22],
                    terasegundo = time_filter[23],
                    yoctosegundo = time_filter[24],
                    yottasegundo = time_filter[25],
                    zeptosegundo = time_filter[26],
                    zettasegundo = time_filter[27],
            )
            time_item.save()
        self.stdout.write(self.style.SUCCESS('Time data loaded to database.'))

