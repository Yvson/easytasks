from django.core.management.base import BaseCommand
from conversor.models import Force

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
    
    def handle(self, *args, **kwargs):
        file = open(kwargs['path'], 'r')
        force = []
        for force_object in file:
            force.append(force_object)

        for force_object in force:
            force_filter = force_object.rstrip().split(',')
            force_item = Force(
                    unit = force_filter[0],
                    attonewton = force_filter[1],
                    centinewton = force_filter[2],
                    decagrama_forca = force_filter[3],
                    decanewton = force_filter[4],
                    decigrama_forca = force_filter[5],
                    decinewton = force_filter[6],
                    dina = force_filter[7],
                    exanewton = force_filter[8],
                    femtonewton = force_filter[9],
                    giganewton = force_filter[10],
                    grama_forca = force_filter[11],
                    hectonewton = force_filter[12],
                    joule_metro = force_filter[13],
                    kip = force_filter[14],
                    libra_forca = force_filter[15],
                    meganewton = force_filter[16],
                    megapond = force_filter[17],
                    micronewton = force_filter[18],
                    milinewton = force_filter[19],
                    nanonewton = force_filter[20],
                    newton = force_filter[21],
                    onca_forca = force_filter[22],
                    petanewton = force_filter[23],
                    piconewton = force_filter[24],
                    pond = force_filter[25],
                    poundal = force_filter[26],
                    quilograma_forca = force_filter[27],
                    quilonewton = force_filter[28],
                    quilopond = force_filter[29],
                    sthene = force_filter[30],
                    teranewton = force_filter[31],
                    tonelada_forca = force_filter[32],
                    yoctonewton = force_filter[33],
                    yottanewton = force_filter[34],
                    zeptonewton = force_filter[35],
                    zettanewton = force_filter[36]
                )
            force_item.save()
        self.stdout.write(self.style.SUCCESS('Force data loaded to database.'))

