from django.core.management.base import BaseCommand
from conversor.models import Volume

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
    
    def handle(self, *args, **kwargs):
        file = open(kwargs['path'], 'r')
        volume = []
        for volume_object in file:
            volume.append(volume_object)

        for volume_object in volume:
            volume_filter = volume_object.rstrip().split(',')
            volume_item = Volume(
                    unit = volume_filter[0],
                    angstrom_3 = volume_filter[1],
                    ano_luz_3 = volume_filter[2],
                    attometro_3 = volume_filter[3],
                    centilitro = volume_filter[4],
                    centimetro_3 = volume_filter[5],
                    colher_de_cha_americana = volume_filter[6],
                    colher_de_cha_imperial = volume_filter[7],
                    colher_de_sopa_americana = volume_filter[8],
                    colher_de_sopa_imperial = volume_filter[9],
                    decametro_3 = volume_filter[10],
                    decilitro = volume_filter[11],
                    decimetro_3 = volume_filter[12],
                    exametro_3 = volume_filter[13],
                    femtometro_3 = volume_filter[14],
                    galao_americano = volume_filter[15],
                    galao_imperial = volume_filter[16],
                    gigametro_3 = volume_filter[17],
                    hectometro_3 = volume_filter[18],
                    jardas_3 = volume_filter[19],
                    litro = volume_filter[20],
                    megametro_3 = volume_filter[21],
                    metro_3 = volume_filter[22],
                    micrometro_3 = volume_filter[23],
                    milha_nautica_3 = volume_filter[24],
                    milhas_3 = volume_filter[25],
                    mililitro = volume_filter[26],
                    milimetro_3 = volume_filter[27],
                    nanometro_3 = volume_filter[28],
                    onca_liquida_americana = volume_filter[29],
                    onca_liquida_imperial = volume_filter[30],
                    parsec_3 = volume_filter[31],
                    pe_3 = volume_filter[32],
                    petametro_3 = volume_filter[33],
                    picometro_3 = volume_filter[34],
                    polegadas_3 = volume_filter[35],
                    quartilho_americano = volume_filter[36],
                    quartilho_imperial = volume_filter[37],
                    quarto_imperial = volume_filter[38],
                    quarto_liquido_americano = volume_filter[39],
                    quilometro_3 = volume_filter[40],
                    terametro_3 = volume_filter[41],
                    unidade_astronomica_3 = volume_filter[42],
                    xicara_americana = volume_filter[43],
                    xicara_imperial = volume_filter[44],
                    yoctometro_3 = volume_filter[45],
                    yottametro_3 = volume_filter[46],
                    zeptometro_3 = volume_filter[47],
                    zettametro_3 = volume_filter[48]
                )
            volume_item.save()
        self.stdout.write(self.style.SUCCESS('Volume data loaded to database.'))

