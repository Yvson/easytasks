from django.core.management.base import BaseCommand
from conversor.models import Area

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
    
    def handle(self, *args, **kwargs):
        file = open(kwargs['path'], 'r')
        area = []
        for area_object in file:
            area.append(area_object)

        for area_object in area:
            area_filter = area_object.rstrip().split(',')
            area_item = Area(
                    unit = area_filter[0],
                    acre = area_filter[1],
                    angstrom_2 = area_filter[2],
                    ano_luz_2 = area_filter[3],
                    attometro_2 = area_filter[4],
                    centimetro_2 = area_filter[5],
                    decametro_2 = area_filter[6],
                    decimetro_2 = area_filter[7],
                    exametro_2 = area_filter[8],
                    femtometro_2 = area_filter[9],
                    gigametro_2 = area_filter[10],
                    hectare = area_filter[11],
                    hectometro_2 = area_filter[12],
                    jardas_2 = area_filter[13],
                    megametro_2 = area_filter[14],
                    metro_2 = area_filter[15],
                    micrometro_2 = area_filter[16],
                    milha_nautica_2 = area_filter[17],
                    milhas_2 = area_filter[18],
                    milimetro_2 = area_filter[19],
                    nanometro_2 = area_filter[20],
                    parsec_2 = area_filter[21],
                    pe_2 = area_filter[22],
                    petametro_2 = area_filter[23],
                    picometro_2 = area_filter[24],
                    polegadas_2 = area_filter[25],
                    quilometro_2 = area_filter[26],
                    terametro_2 = area_filter[27],
                    unidade_astronomica_2 = area_filter[28],
                    yoctometro_2 = area_filter[29],
                    yottametro_2 = area_filter[30],
                    zeptometro_2 = area_filter[31],
                    zettametro_2 = area_filter[32],
            )
            area_item.save()
        self.stdout.write(self.style.SUCCESS('Area data loaded to database.'))

