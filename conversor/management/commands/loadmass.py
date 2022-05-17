from django.core.management.base import BaseCommand
from conversor.models import Mass

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
    
    def handle(self, *args, **kwargs):
        file = open(kwargs['path'], 'r')
        mass = []
        for mass_object in file:
            mass.append(mass_object)

        for mass_object in mass:
            mass_filter = mass_object.rstrip().split(',')
            mass_item = Mass(
                    unit=mass_filter[0],
                    attograma = mass_filter[1],
                    centigrama = mass_filter[2],
                    dalton = mass_filter[3],
                    decagrama = mass_filter[4],
                    decigrama = mass_filter[5],
                    exagrama = mass_filter[6],
                    femtograma = mass_filter[7],
                    gigagrama = mass_filter[8],
                    grama = mass_filter[9],
                    hectograma = mass_filter[10],
                    libra = mass_filter[11],
                    megagrama = mass_filter[12],
                    micrograma = mass_filter[13],
                    miligrama = mass_filter[14],
                    nanograma = mass_filter[15],
                    onca = mass_filter[16],
                    onca_troy = mass_filter[17],
                    petagrama = mass_filter[18],
                    picograma = mass_filter[19],
                    quilograma = mass_filter[20],
                    slug = mass_filter[21],
                    stone = mass_filter[22],
                    teragrama = mass_filter[23],
                    tonelada = mass_filter[24],
                    tonelada_curta = mass_filter[25],
                    tonelada_longa = mass_filter[26],
                    yoctograma = mass_filter[27],
                    yottagrama = mass_filter[28],
                    zeptograma = mass_filter[29],
                    zettagrama = mass_filter[30]
            )
            mass_item.save()
        self.stdout.write(self.style.SUCCESS('Mass data loaded to database.'))

