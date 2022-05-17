from django.contrib import admin
from .models import Mass, Time, Length, \
    Area, Volume, Velocity, Acceleration, \
    Force, Pressure, Temperature, Conversion



@admin.register(Conversion)
class ConversionAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'profile', 'unit_from', 'unit_to']


@admin.register(Mass)
class MassAdmin(admin.ModelAdmin):
    list_display = ['unit',
                    'attograma',
                    'centigrama',
                    'dalton',
                    'decagrama',
                    'decigrama',
                    'exagrama',
                    'femtograma',
                    'gigagrama',
                    'grama',
                    'hectograma',
                    'libra',
                    'megagrama',
                    'micrograma',
                    'miligrama',
                    'nanograma',
                    'onca',
                    'onca_troy',
                    'petagrama',
                    'picograma',
                    'quilograma',
                    'slug',
                    'stone',
                    'teragrama',
                    'tonelada',
                    'tonelada_curta',
                    'tonelada_longa',
                    'yoctograma',
                    'yottagrama',
                    'zeptograma',
                    'zettagrama'                    
                    ]


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ['unit',
                    'segundo',
                    'yoctosegundo',
                    'zeptosegundo',
                    'attosegundo',
                    'femtosegundo',
                    'picosegundo',
                    'nanosegundo',
                    'microsegundo',
                    'milisegundo',
                    'centisegundo',
                    'decisegundo',
                    'decasegundo',
                    'hectosegundo',
                    'quilosegundo',
                    'megasegundo',
                    'gigasegundo',
                    'terasegundo',
                    'petasegundo',
                    'exasegundo',
                    'zettasegundo',
                    'yottasegundo',
                    'minuto',
                    'hora',
                    'dia',
                    'semana',
                    'mes',
                    'ano',
                    ]


@admin.register(Length)
class LengthAdmin(admin.ModelAdmin):
    list_display = ['unit',
                    'angstrom',
                    'ano_luz',
                    'attometro',
                    'centimetro',
                    'decametro',
                    'decimetro',
                    'exametro',
                    'femtometro',
                    'gigametro',
                    'hectometro',
                    'jardas',
                    'megametro',
                    'metro',
                    'micrometro',
                    'milha',
                    'milha_nautica',
                    'milimetro',
                    'nanometro',
                    'parsec',
                    'pe',
                    'petametro',
                    'picometro',
                    'quilometro',
                    'polegada',
                    'terametro',
                    'unidade_astronomica',
                    'yoctometro',
                    'yottametro',
                    'zeptometro',
                    'zettametro',
                    ]


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['unit',
                    'acre',
                    'angstrom_2',
                    'ano_luz_2',
                    'attometro_2',
                    'centimetro_2',
                    'decametro_2',
                    'decimetro_2',
                    'exametro_2',
                    'femtometro_2',
                    'gigametro_2',
                    'hectare',
                    'hectometro_2',
                    'jardas_2',
                    'megametro_2',
                    'metro_2',
                    'micrometro_2',
                    'milha_nautica_2',
                    'milhas_2',
                    'milimetro_2',
                    'nanometro_2',
                    'parsec_2',
                    'pe_2',
                    'petametro_2',
                    'picometro_2',
                    'polegadas_2',
                    'quilometro_2',
                    'terametro_2',
                    'unidade_astronomica_2',
                    'yoctometro_2',
                    'yottametro_2',
                    'zeptometro_2',
                    'zettametro_2',
                    ]


@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ['unit',
                    'angstrom_3',
                    'ano_luz_3',
                    'attometro_3',
                    'centilitro',
                    'centimetro_3',
                    'colher_de_cha_americana',
                    'colher_de_cha_imperial',
                    'colher_de_sopa_americana',
                    'colher_de_sopa_imperial',
                    'decametro_3',
                    'decilitro',
                    'decimetro_3',
                    'exametro_3',
                    'femtometro_3',
                    'galao_americano',
                    'galao_imperial',
                    'gigametro_3',
                    'hectometro_3',
                    'jardas_3',
                    'litro',
                    'megametro_3',
                    'metro_3',
                    'micrometro_3',
                    'milha_nautica_3',
                    'milhas_3',
                    'mililitro',
                    'milimetro_3',
                    'nanometro_3',
                    'onca_liquida_americana',
                    'onca_liquida_imperial',
                    'parsec_3',
                    'pe_3',
                    'petametro_3',
                    'picometro_3',
                    'polegadas_3',
                    'quartilho_americano',
                    'quartilho_imperial',
                    'quarto_imperial',
                    'quarto_liquido_americano',
                    'quilometro_3',
                    'terametro_3',
                    'unidade_astronomica_3',
                    'xicara_americana',
                    'xicara_imperial',
                    'yoctometro_3',
                    'yottametro_3',
                    'zeptometro_3',
                    'zettametro_3'
                    ]


@admin.register(Velocity)
class VelocityAdmin(admin.ModelAdmin):
    list_display = ['unit',
                    'cm_h',
                    'cm_min',
                    'cm_ms',
                    'cm_s',
                    'ft_h',
                    'ft_min',
                    'ft_ms',
                    'ft_ns',
                    'ft_s',
                    'ft_us',
                    'in_ms',
                    'in_ns',
                    'in_s',
                    'in_us',
                    'km_h',
                    'km_min',
                    'km_ms',
                    'km_ns',
                    'km_s',
                    'km_us',
                    'lea_h',
                    'lea_s',
                    'm_h',
                    'm_min',
                    'm_ms',
                    'm_ns',
                    'm_s',
                    'm_us',
                    'mi_h',
                    'mi_min',
                    'mi_ms',
                    'mi_ns',
                    'mi_s',
                    'mi_us',
                    'mm_ms',
                    'mm_ns',
                    'mm_s',
                    'mm_us',
                    'nm_ms',
                    'nm_ns',
                    'nm_s',
                    'nm_us',
                    'um_ms',
                    'um_ns',
                    'um_s',
                    'um_us',
                    'yd_min',
                    'yd_ms',
                    'yd_ns',
                    'yd_s',
                    'yd_us'
                    ]


@admin.register(Acceleration)
class AccelerationAdmin(admin.ModelAdmin):
    list_display = ['unit',
                    'cm_ms2',
                    'cm_s2',
                    'ft_h2',
                    'ft_min2',
                    'ft_ms2',
                    'ft_ns2',
                    'ft_s2',
                    'ft_us2',
                    'g',
                    'gal',
                    'in_ms2',
                    'in_ns2',
                    'in_s2',
                    'in_us2',
                    'km_h2',
                    'km_min2',
                    'km_ms2',
                    'km_ns2',
                    'km_s2',
                    'km_us2',
                    'lea_h2',
                    'lea_s2',
                    'm_h2',
                    'm_min2',
                    'm_ms2',
                    'm_ns2',
                    'm_s2',
                    'm_us2',
                    'mi_h2',
                    'mi_min2',
                    'mi_ms2',
                    'mi_ns2',
                    'mi_s2',
                    'mi_us2',
                    'mm_ms2',
                    'mm_ns2',
                    'mm_s2',
                    'mm_us2',
                    'nm_ms2',
                    'nm_ns2',
                    'nm_s2',
                    'nm_us2',
                    'um_ms2',
                    'um_ns2',
                    'um_s2',
                    'um_us2',
                    'yd_min2',
                    'yd_ms2',
                    'yd_ns2',
                    'yd_s2',
                    'yd_us2'
                    ]


@admin.register(Force)
class ForceAdmin(admin.ModelAdmin):
    list_display = ['unit',
                    'attonewton',
                    'centinewton',
                    'decagrama_forca',
                    'decanewton',
                    'decigrama_forca',
                    'decinewton',
                    'dina',
                    'exanewton',
                    'femtonewton',
                    'giganewton',
                    'grama_forca',
                    'hectonewton',
                    'joule_metro',
                    'quilograma_forca',
                    'kip',
                    'libra_forca',
                    'meganewton',
                    'megapond',
                    'micronewton',
                    'milinewton',
                    'nanonewton',
                    'newton',
                    'onca_forca',
                    'petanewton',
                    'piconewton',
                    'pond',
                    'poundal',
                    'quilonewton',
                    'quilopond',
                    'sthene',
                    'teranewton',
                    'tonelada_forca',
                    'yoctonewton',
                    'yottanewton',
                    'zeptonewton',
                    'zettanewton'
                    ]


@admin.register(Pressure)
class PressureAdmin(admin.ModelAdmin):
    list_display = ['unit',
                    'atmosfera_padrao',
                    'atmosfera_tecnico',
                    'attobar',
                    'attopascal',
                    'bar',
                    'barad',
                    'barye',
                    'centibar',
                    'centihg',
                    'centimetro_de_agua_4_C',
                    'centimetro_de_mercurio_0_C',
                    'centipascal',
                    'centitorr',
                    'coluna_de_agua_centimetro',
                    'coluna_de_agua_milimetro',
                    'coluna_de_agua_polegada',
                    'decabar',
                    'decapascal',
                    'decibar',
                    'decipascal',
                    'decitorr',
                    'dina_centimetro_ao_quadrado',
                    'exabar',
                    'exapascal',
                    'femtobar',
                    'femtopascal',
                    'gigabar',
                    'gigapascal',
                    'grama_forca_centimetro_ao_quadrado',
                    'hectobar',
                    'hectopascal',
                    'kip_pe_ao_quadrado',
                    'kip_polegada_ao_quadrado',
                    'libra_pe_ao_quadrado',
                    'libra_polegada_ao_quadrado',
                    'megabar',
                    'meganewton_metro_ao_quadrado',
                    'megapascal',
                    'metro_de_ar_0_C',
                    'metro_de_ar_15_C',
                    'microbar',
                    'micrometro_de_agua_4_C',
                    'micrometro_de_mercurio_0_C',
                    'micropascal',
                    'milibar',
                    'milihg',
                    'milimetro_de_agua_4_C',
                    'milimetro_de_mercurio_0_C',
                    'milipascal',
                    'militorr',
                    'nanobar',
                    'nanopascal',
                    'newton_metro_ao_quadrado',
                    'newton_milimetro_ao_quadrado',
                    'onca_polegada_ao_quadrado',
                    'pascal',
                    'pe_de_agua_4_C',
                    'pe_de_ar_0_C',
                    'pe_de_ar_15_C',
                    'pe_de_mercurio_0_C',
                    'petabar',
                    'petapascal',
                    'picobar',
                    'picopascal',
                    'pieze',
                    'polegada_de_agua_4_C',
                    'polegada_de_ar_0_C',
                    'polegada_de_ar_15_C',
                    'polegada_de_mercurio_0_C',
                    'poundal_pe_ao_quadrado',
                    'quilobar',
                    'quilograma_forca_centimetro_ao_quadrado',
                    'quilograma_forca_metro_ao_quadrado',
                    'quilograma_forca_milimetro_ao_quadrado',
                    'quilonewton_metro_ao_quadrado',
                    'quilopascal',
                    'quilopond_centimetro_ao_quadrado',
                    'quilopond_metro_ao_quadrado',
                    'quilopond_milimetro_ao_quadrado',
                    'sthene_metro_ao_quadrado',
                    'terabar',
                    'terapascal',
                    'tonelada_curta_pe_ao_quadrado',
                    'tonelada_curta_polegada_ao_quadrado',
                    'tonelada_longa_pe_ao_quadrado',
                    'tonelada_longa_polegada_ao_quadrado',
                    'tonelada_metro_ao_quadrado',
                    'torr',
                    'yoctobar',
                    'yoctopascal',
                    'yottabar',
                    'yottapascal',
                    'zeptobar',
                    'zeptopascal',
                    'zettabar',
                    'zettapascal'
                    ]


@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):
    list_display = ['unit',
                    'kelvin',
                    'celsius',
                    'fahrenheit',
                    'rankine',
                    'reaumur',
                    'romer',
                    'newton',
                    'delisle'
                    ]
