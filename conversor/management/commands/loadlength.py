from django.core.management.base import BaseCommand
from conversor.models import Length

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
    
    def handle(self, *args, **kwargs):
        file = open(kwargs['path'], 'r')
        length = []
        for length_object in file:
            length.append(length_object)

        for length_object in length:
            length_filter = length_object.rstrip().split(',')
            length_item = Length(
                    unit = length_filter[0],
                    angstrom = length_filter[1],
                    ano_luz = length_filter[2],
                    attometro = length_filter[3],
                    centimetro = length_filter[4],
                    decametro = length_filter[5],
                    decimetro = length_filter[6],
                    exametro = length_filter[7],
                    femtometro = length_filter[8],
                    gigametro = length_filter[9],
                    hectometro = length_filter[10],
                    jardas = length_filter[11],
                    megametro = length_filter[12],
                    metro = length_filter[13],
                    micrometro = length_filter[14],
                    milha = length_filter[15],
                    milha_nautica = length_filter[16],
                    milimetro = length_filter[17],
                    nanometro = length_filter[18],
                    parsec = length_filter[19],
                    pe = length_filter[20],
                    petametro = length_filter[21],
                    picometro = length_filter[22],
                    polegada = length_filter[23],
                    quilometro = length_filter[24],
                    terametro = length_filter[25],
                    unidade_astronomica = length_filter[26],
                    yoctometro = length_filter[27],
                    yottametro = length_filter[28],
                    zeptometro = length_filter[29],
                    zettametro = length_filter[30],
            )
            length_item.save()
        self.stdout.write(self.style.SUCCESS('Length data loaded to database.'))

