from django.core.management.base import BaseCommand
from conversor.models import Velocity

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
    
    def handle(self, *args, **kwargs):
        file = open(kwargs['path'], 'r')
        velocity = []
        for velocity_object in file:
            velocity.append(velocity_object)

        for velocity_object in velocity:
            velocity_filter = velocity_object.rstrip().split(',')
            velocity_item = Velocity(
                    unit = velocity_filter[0],
                    cm_h = velocity_filter[1],
                    cm_min = velocity_filter[2],
                    cm_ms = velocity_filter[3],
                    cm_s = velocity_filter[4],
                    ft_h = velocity_filter[5],
                    ft_min = velocity_filter[6],
                    ft_ms = velocity_filter[7],
                    ft_ns = velocity_filter[8],
                    ft_s = velocity_filter[9],
                    ft_us = velocity_filter[10],
                    in_ms = velocity_filter[11],
                    in_ns = velocity_filter[12],
                    in_s = velocity_filter[13],
                    in_us = velocity_filter[14],
                    km_h = velocity_filter[15],
                    km_min = velocity_filter[16],
                    km_ms = velocity_filter[17],
                    km_ns = velocity_filter[18],
                    km_s = velocity_filter[19],
                    km_us = velocity_filter[20],
                    lea_h = velocity_filter[21],
                    lea_s = velocity_filter[22],
                    m_h = velocity_filter[23],
                    m_min = velocity_filter[24],
                    m_ms = velocity_filter[25],
                    m_ns = velocity_filter[26],
                    m_s = velocity_filter[27],
                    m_us = velocity_filter[28],
                    mi_h = velocity_filter[29],
                    mi_min = velocity_filter[30],
                    mi_ms = velocity_filter[31],
                    mi_ns = velocity_filter[32],
                    mi_s = velocity_filter[33],
                    mi_us = velocity_filter[34],
                    mm_ms = velocity_filter[35],
                    mm_ns = velocity_filter[36],
                    mm_s = velocity_filter[37],
                    mm_us = velocity_filter[38],
                    nm_ms = velocity_filter[39],
                    nm_ns = velocity_filter[40],
                    nm_s = velocity_filter[41],
                    nm_us = velocity_filter[42],
                    um_ms = velocity_filter[43],
                    um_ns = velocity_filter[44],
                    um_s = velocity_filter[45],
                    um_us = velocity_filter[46],
                    yd_min = velocity_filter[47],
                    yd_ms = velocity_filter[48],
                    yd_ns = velocity_filter[49],
                    yd_s = velocity_filter[50],
                    yd_us = velocity_filter[51]
                )
            velocity_item.save()
        self.stdout.write(self.style.SUCCESS('Velocity data loaded to database.'))

