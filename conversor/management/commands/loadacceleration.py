from django.core.management.base import BaseCommand
from conversor.models import Acceleration

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
    
    def handle(self, *args, **kwargs):
        file = open(kwargs['path'], 'r')
        acceleration = []
        for acceleration_object in file:
            acceleration.append(acceleration_object)

        for acceleration_object in acceleration:
            acceleration_filter = acceleration_object.rstrip().split(',')
            acceleration_item = Acceleration(
                    unit = acceleration_filter[0],
                    cm_ms2 = acceleration_filter[1],
                    cm_s2 = acceleration_filter[2],
                    ft_h2 = acceleration_filter[3],
                    ft_min2 = acceleration_filter[4],
                    ft_ms2 = acceleration_filter[5],
                    ft_ns2 = acceleration_filter[6],
                    ft_s2 = acceleration_filter[7],
                    ft_us2 = acceleration_filter[8],
                    g = acceleration_filter[9],
                    gal = acceleration_filter[10],
                    in_ms2 = acceleration_filter[11],
                    in_ns2 = acceleration_filter[12],
                    in_s2 = acceleration_filter[13],
                    in_us2 = acceleration_filter[14],
                    km_h2 = acceleration_filter[15],
                    km_min2 = acceleration_filter[16],
                    km_ms2 = acceleration_filter[17],
                    km_ns2 = acceleration_filter[18],
                    km_s2 = acceleration_filter[19],
                    km_us2 = acceleration_filter[20],
                    lea_h2 = acceleration_filter[21],
                    lea_s2 = acceleration_filter[22],
                    m_h2 = acceleration_filter[23],
                    m_min2 = acceleration_filter[24],
                    m_ms2 = acceleration_filter[25],
                    m_ns2 = acceleration_filter[26],
                    m_s2 = acceleration_filter[27],
                    m_us2 = acceleration_filter[28],
                    mi_h2 = acceleration_filter[29],
                    mi_min2 = acceleration_filter[30],
                    mi_ms2 = acceleration_filter[31],
                    mi_ns2 = acceleration_filter[32],
                    mi_s2 = acceleration_filter[33],
                    mi_us2 = acceleration_filter[34],
                    mm_ms2 = acceleration_filter[35],
                    mm_ns2 = acceleration_filter[36],
                    mm_s2 = acceleration_filter[37],
                    mm_us2 = acceleration_filter[38],
                    nm_ms2 = acceleration_filter[39],
                    nm_ns2 = acceleration_filter[40],
                    nm_s2 = acceleration_filter[41],
                    nm_us2 = acceleration_filter[42],
                    um_ms2 = acceleration_filter[43],
                    um_ns2 = acceleration_filter[44],
                    um_s2 = acceleration_filter[45],
                    um_us2 = acceleration_filter[46],
                    yd_min2 = acceleration_filter[47],
                    yd_ms2 = acceleration_filter[48],
                    yd_ns2 = acceleration_filter[49],
                    yd_s2 = acceleration_filter[50],
                    yd_us2 = acceleration_filter[51],
                    
                )
            acceleration_item.save()
        self.stdout.write(self.style.SUCCESS('Acceleration data loaded to database.'))

