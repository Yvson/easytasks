from django.db import models
from django.db.models import Count
from django.core.exceptions import ValidationError

from conta.models import Profile


class Conversion(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile,
                                related_name='conversions',
                                on_delete=models.CASCADE)
    unit_from = models.CharField(max_length=50)
    unit_to = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Conversion'
        verbose_name_plural = 'Conversions'
        ordering = ["-date"]

    def __str__(self):
        return f'Conversions for user {self.profile.user.username}'

    def save(self, profile_id=None, *args, **kwargs):
        profile_conversions = Profile.objects.filter(id=self.profile.id).annotate(qty_entries=Count('conversions'))
        if profile_conversions[0].qty_entries >= 15:
            raise ValidationError(
                'Exceeded maximum limit of entries',
                code='Exceeded limit')
        super().save(self, *args, **kwargs)


class Mass(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit = models.CharField(max_length=100)
    attograma = models.DecimalField(max_digits=150, decimal_places=80)
    centigrama = models.DecimalField(max_digits=150, decimal_places=80)
    dalton = models.DecimalField(max_digits=150, decimal_places=80)
    decagrama = models.DecimalField(max_digits=150, decimal_places=80)
    decigrama = models.DecimalField(max_digits=150, decimal_places=80)
    exagrama = models.DecimalField(max_digits=150, decimal_places=80)
    femtograma = models.DecimalField(max_digits=150, decimal_places=80)
    gigagrama = models.DecimalField(max_digits=150, decimal_places=80)
    grama = models.DecimalField(max_digits=150, decimal_places=80)
    hectograma = models.DecimalField(max_digits=150, decimal_places=80)
    libra = models.DecimalField(max_digits=150, decimal_places=80)
    megagrama = models.DecimalField(max_digits=150, decimal_places=80)
    micrograma = models.DecimalField(max_digits=150, decimal_places=80)
    miligrama = models.DecimalField(max_digits=150, decimal_places=80)
    nanograma = models.DecimalField(max_digits=150, decimal_places=80)
    onca = models.DecimalField(max_digits=150, decimal_places=80)
    onca_troy = models.DecimalField(max_digits=150, decimal_places=80)
    petagrama = models.DecimalField(max_digits=150, decimal_places=80)
    picograma = models.DecimalField(max_digits=150, decimal_places=80)
    quilograma = models.DecimalField(max_digits=150, decimal_places=80)    
    slug = models.DecimalField(max_digits=150, decimal_places=80)
    stone = models.DecimalField(max_digits=150, decimal_places=80)
    teragrama = models.DecimalField(max_digits=150, decimal_places=80)
    tonelada = models.DecimalField(max_digits=150, decimal_places=80)
    tonelada_curta = models.DecimalField(max_digits=150, decimal_places=80)
    tonelada_longa = models.DecimalField(max_digits=150, decimal_places=80)
    yoctograma = models.DecimalField(max_digits=150, decimal_places=80)
    yottagrama = models.DecimalField(max_digits=150, decimal_places=80)
    zeptograma = models.DecimalField(max_digits=150, decimal_places=80)
    zettagrama = models.DecimalField(max_digits=150, decimal_places=80)

    class Meta:
        verbose_name = 'Mass'
        verbose_name_plural = 'Mass'
        ordering = ["id"]

    def __str__(self):
        return self.unit


class Time(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit = models.CharField(max_length=100)
    ano = models.DecimalField(max_digits=150, decimal_places=80)
    attosegundo = models.DecimalField(max_digits=150, decimal_places=80)
    centisegundo = models.DecimalField(max_digits=150, decimal_places=80)
    decasegundo = models.DecimalField(max_digits=150, decimal_places=80)
    decisegundo = models.DecimalField(max_digits=150, decimal_places=80)
    dia = models.DecimalField(max_digits=150, decimal_places=80)
    exasegundo = models.DecimalField(max_digits=150, decimal_places=80)
    femtosegundo = models.DecimalField(max_digits=150, decimal_places=80)
    gigasegundo = models.DecimalField(max_digits=150, decimal_places=80)
    hectosegundo = models.DecimalField(max_digits=150, decimal_places=80)
    hora = models.DecimalField(max_digits=150, decimal_places=80)
    megasegundo = models.DecimalField(max_digits=150, decimal_places=80)
    mes = models.DecimalField(max_digits=150, decimal_places=80)
    microsegundo = models.DecimalField(max_digits=150, decimal_places=80)
    milisegundo = models.DecimalField(max_digits=150, decimal_places=80)
    minuto = models.DecimalField(max_digits=150, decimal_places=80)
    nanosegundo = models.DecimalField(max_digits=150, decimal_places=80)
    petasegundo = models.DecimalField(max_digits=150, decimal_places=80)
    picosegundo = models.DecimalField(max_digits=150, decimal_places=80)
    quilosegundo = models.DecimalField(max_digits=150, decimal_places=80)
    segundo = models.DecimalField(max_digits=150, decimal_places=80)
    semana = models.DecimalField(max_digits=150, decimal_places=80)
    terasegundo = models.DecimalField(max_digits=150, decimal_places=80)
    yoctosegundo = models.DecimalField(max_digits=150, decimal_places=80)
    yottasegundo = models.DecimalField(max_digits=150, decimal_places=80)
    zeptosegundo = models.DecimalField(max_digits=150, decimal_places=80)
    zettasegundo = models.DecimalField(max_digits=150, decimal_places=80)

    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Time'
        ordering = ["id"]

    def __str__(self):
        return self.unit


class Length(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit = models.CharField(max_length=100)
    angstrom = models.DecimalField(max_digits=150, decimal_places=80)
    ano_luz = models.DecimalField(max_digits=150, decimal_places=80)
    attometro = models.DecimalField(max_digits=150, decimal_places=80)
    centimetro = models.DecimalField(max_digits=150, decimal_places=80)
    decametro = models.DecimalField(max_digits=150, decimal_places=80)
    decimetro = models.DecimalField(max_digits=150, decimal_places=80)
    exametro = models.DecimalField(max_digits=150, decimal_places=80)
    femtometro = models.DecimalField(max_digits=150, decimal_places=80)
    gigametro = models.DecimalField(max_digits=150, decimal_places=80)
    hectometro = models.DecimalField(max_digits=150, decimal_places=80)
    jardas = models.DecimalField(max_digits=150, decimal_places=80)
    megametro = models.DecimalField(max_digits=150, decimal_places=80)
    metro = models.DecimalField(max_digits=150, decimal_places=80)
    micrometro = models.DecimalField(max_digits=150, decimal_places=80)
    milha = models.DecimalField(max_digits=150, decimal_places=80)
    milha_nautica = models.DecimalField(max_digits=150, decimal_places=80)
    milimetro = models.DecimalField(max_digits=150, decimal_places=80)
    nanometro = models.DecimalField(max_digits=150, decimal_places=80)
    parsec = models.DecimalField(max_digits=150, decimal_places=80)
    pe = models.DecimalField(max_digits=150, decimal_places=80)
    petametro = models.DecimalField(max_digits=150, decimal_places=80)
    picometro = models.DecimalField(max_digits=150, decimal_places=80)
    polegada = models.DecimalField(max_digits=150, decimal_places=80)
    quilometro = models.DecimalField(max_digits=150, decimal_places=80)
    terametro = models.DecimalField(max_digits=150, decimal_places=80)
    unidade_astronomica = models.DecimalField(
        max_digits=150, decimal_places=80)
    yoctometro = models.DecimalField(max_digits=150, decimal_places=80)
    yottametro = models.DecimalField(max_digits=150, decimal_places=80)
    zeptometro = models.DecimalField(max_digits=150, decimal_places=80)
    zettametro = models.DecimalField(max_digits=150, decimal_places=80)

    class Meta:
        verbose_name = 'Length'
        verbose_name_plural = 'Length'
        ordering = ["id"]

    def __str__(self):
        return self.unit


class Area(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit = models.CharField(max_length=100)
    acre = models.DecimalField(max_digits=300, decimal_places=150)
    angstrom_2 = models.DecimalField(max_digits=300, decimal_places=150)
    ano_luz_2 = models.DecimalField(max_digits=300, decimal_places=150)
    attometro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    centimetro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    decametro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    decimetro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    exametro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    femtometro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    gigametro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    hectare = models.DecimalField(max_digits=300, decimal_places=150)
    hectometro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    jardas_2 = models.DecimalField(max_digits=300, decimal_places=150)
    megametro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    metro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    micrometro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    milha_nautica_2 = models.DecimalField(max_digits=300, decimal_places=150)
    milhas_2 = models.DecimalField(max_digits=300, decimal_places=150)
    milimetro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    nanometro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    parsec_2 = models.DecimalField(max_digits=300, decimal_places=150)
    pe_2 = models.DecimalField(max_digits=300, decimal_places=150)
    petametro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    picometro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    polegadas_2 = models.DecimalField(max_digits=300, decimal_places=150)
    quilometro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    terametro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    unidade_astronomica_2 = models.DecimalField(
        max_digits=300, decimal_places=150)
    yoctometro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    yottametro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    zeptometro_2 = models.DecimalField(max_digits=300, decimal_places=150)
    zettametro_2 = models.DecimalField(max_digits=300, decimal_places=150)

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Area'
        ordering = ["id"]

    def __str__(self):
        return self.unit


class Volume(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit = models.CharField(max_length=100)
    angstrom_3 = models.DecimalField(max_digits=300, decimal_places=150)
    ano_luz_3 = models.DecimalField(max_digits=300, decimal_places=150)
    attometro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    centilitro = models.DecimalField(max_digits=300, decimal_places=150)
    centimetro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    colher_de_cha_americana = models.DecimalField(
        max_digits=300, decimal_places=150)
    colher_de_cha_imperial = models.DecimalField(
        max_digits=300, decimal_places=150)
    colher_de_sopa_americana = models.DecimalField(
        max_digits=300, decimal_places=150)
    colher_de_sopa_imperial = models.DecimalField(
        max_digits=300, decimal_places=150)
    decametro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    decilitro = models.DecimalField(max_digits=300, decimal_places=150)
    decimetro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    exametro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    femtometro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    galao_americano = models.DecimalField(max_digits=300, decimal_places=150)
    galao_imperial = models.DecimalField(max_digits=300, decimal_places=150)
    gigametro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    hectometro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    jardas_3 = models.DecimalField(max_digits=300, decimal_places=150)
    litro = models.DecimalField(max_digits=300, decimal_places=150)
    megametro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    metro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    micrometro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    milha_nautica_3 = models.DecimalField(max_digits=300, decimal_places=150)
    milhas_3 = models.DecimalField(max_digits=300, decimal_places=150)
    mililitro = models.DecimalField(max_digits=300, decimal_places=150)
    milimetro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    nanometro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    onca_liquida_americana = models.DecimalField(
        max_digits=300, decimal_places=150)
    onca_liquida_imperial = models.DecimalField(
        max_digits=300, decimal_places=150)
    parsec_3 = models.DecimalField(max_digits=300, decimal_places=150)
    pe_3 = models.DecimalField(max_digits=300, decimal_places=150)
    petametro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    picometro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    polegadas_3 = models.DecimalField(max_digits=300, decimal_places=150)
    quartilho_americano = models.DecimalField(
        max_digits=300, decimal_places=150)
    quartilho_imperial = models.DecimalField(
        max_digits=300, decimal_places=150)
    quarto_imperial = models.DecimalField(max_digits=300, decimal_places=150)
    quarto_liquido_americano = models.DecimalField(
        max_digits=300, decimal_places=150)
    quilometro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    terametro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    unidade_astronomica_3 = models.DecimalField(
        max_digits=300, decimal_places=150)
    xicara_americana = models.DecimalField(max_digits=300, decimal_places=150)
    xicara_imperial = models.DecimalField(max_digits=300, decimal_places=150)
    yoctometro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    yottametro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    zeptometro_3 = models.DecimalField(max_digits=300, decimal_places=150)
    zettametro_3 = models.DecimalField(max_digits=300, decimal_places=150)

    class Meta:
        verbose_name = 'Volume'
        verbose_name_plural = 'Volume'
        ordering = ["id"]

    def __str__(self):
        return self.unit


class Velocity(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit = models.CharField(max_length=100)
    cm_h = models.DecimalField(max_digits=300, decimal_places=150)
    cm_min = models.DecimalField(max_digits=300, decimal_places=150)
    cm_ms = models.DecimalField(max_digits=300, decimal_places=150)
    cm_s = models.DecimalField(max_digits=300, decimal_places=150)
    ft_h = models.DecimalField(max_digits=300, decimal_places=150)
    ft_min = models.DecimalField(max_digits=300, decimal_places=150)
    ft_ms = models.DecimalField(max_digits=300, decimal_places=150)
    ft_ns = models.DecimalField(max_digits=300, decimal_places=150)
    ft_s = models.DecimalField(max_digits=300, decimal_places=150)
    ft_us = models.DecimalField(max_digits=300, decimal_places=150)
    in_ms = models.DecimalField(max_digits=300, decimal_places=150)
    in_ns = models.DecimalField(max_digits=300, decimal_places=150)
    in_s = models.DecimalField(max_digits=300, decimal_places=150)
    in_us = models.DecimalField(max_digits=300, decimal_places=150)
    km_h = models.DecimalField(max_digits=300, decimal_places=150)
    km_min = models.DecimalField(max_digits=300, decimal_places=150)
    km_ms = models.DecimalField(max_digits=300, decimal_places=150)
    km_ns = models.DecimalField(max_digits=300, decimal_places=150)
    km_s = models.DecimalField(max_digits=300, decimal_places=150)
    km_us = models.DecimalField(max_digits=300, decimal_places=150)
    lea_h = models.DecimalField(max_digits=300, decimal_places=150)
    lea_s = models.DecimalField(max_digits=300, decimal_places=150)
    m_h = models.DecimalField(max_digits=300, decimal_places=150)
    m_min = models.DecimalField(max_digits=300, decimal_places=150)
    m_ms = models.DecimalField(max_digits=300, decimal_places=150)
    m_ns = models.DecimalField(max_digits=300, decimal_places=150)
    m_s = models.DecimalField(max_digits=300, decimal_places=150)
    m_us = models.DecimalField(max_digits=300, decimal_places=150)
    mi_h = models.DecimalField(max_digits=300, decimal_places=150)
    mi_min = models.DecimalField(max_digits=300, decimal_places=150)
    mi_ms = models.DecimalField(max_digits=300, decimal_places=150)
    mi_ns = models.DecimalField(max_digits=300, decimal_places=150)
    mi_s = models.DecimalField(max_digits=300, decimal_places=150)
    mi_us = models.DecimalField(max_digits=300, decimal_places=150)
    mm_ms = models.DecimalField(max_digits=300, decimal_places=150)
    mm_ns = models.DecimalField(max_digits=300, decimal_places=150)
    mm_s = models.DecimalField(max_digits=300, decimal_places=150)
    mm_us = models.DecimalField(max_digits=300, decimal_places=150)
    nm_ms = models.DecimalField(max_digits=300, decimal_places=150)
    nm_ns = models.DecimalField(max_digits=300, decimal_places=150)
    nm_s = models.DecimalField(max_digits=300, decimal_places=150)
    nm_us = models.DecimalField(max_digits=300, decimal_places=150)
    um_ms = models.DecimalField(max_digits=300, decimal_places=150)
    um_ns = models.DecimalField(max_digits=300, decimal_places=150)
    um_s = models.DecimalField(max_digits=300, decimal_places=150)
    um_us = models.DecimalField(max_digits=300, decimal_places=150)
    yd_min = models.DecimalField(max_digits=300, decimal_places=150)
    yd_ms = models.DecimalField(max_digits=300, decimal_places=150)
    yd_ns = models.DecimalField(max_digits=300, decimal_places=150)
    yd_s = models.DecimalField(max_digits=300, decimal_places=150)
    yd_us = models.DecimalField(max_digits=300, decimal_places=150)

    class Meta:
        verbose_name = 'Velocity'
        verbose_name_plural = 'Velocity'
        ordering = ["id"]

    def __str__(self):
        return self.unit


class Acceleration(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit = models.CharField(max_length=100)
    cm_ms2 = models.DecimalField(max_digits=300, decimal_places=150)
    cm_s2 = models.DecimalField(max_digits=300, decimal_places=150)
    ft_h2 = models.DecimalField(max_digits=300, decimal_places=150)
    ft_min2 = models.DecimalField(max_digits=300, decimal_places=150)
    ft_ms2 = models.DecimalField(max_digits=300, decimal_places=150)
    ft_ns2 = models.DecimalField(max_digits=300, decimal_places=150)
    ft_s2 = models.DecimalField(max_digits=300, decimal_places=150)
    ft_us2 = models.DecimalField(max_digits=300, decimal_places=150)
    g = models.DecimalField(max_digits=300, decimal_places=150)
    gal = models.DecimalField(max_digits=300, decimal_places=150)
    in_ms2 = models.DecimalField(max_digits=300, decimal_places=150)
    in_ns2 = models.DecimalField(max_digits=300, decimal_places=150)
    in_s2 = models.DecimalField(max_digits=300, decimal_places=150)
    in_us2 = models.DecimalField(max_digits=300, decimal_places=150)
    km_h2 = models.DecimalField(max_digits=300, decimal_places=150)
    km_min2 = models.DecimalField(max_digits=300, decimal_places=150)
    km_ms2 = models.DecimalField(max_digits=300, decimal_places=150)
    km_ns2 = models.DecimalField(max_digits=300, decimal_places=150)
    km_s2 = models.DecimalField(max_digits=300, decimal_places=150)
    km_us2 = models.DecimalField(max_digits=300, decimal_places=150)
    lea_h2 = models.DecimalField(max_digits=300, decimal_places=150)
    lea_s2 = models.DecimalField(max_digits=300, decimal_places=150)
    m_h2 = models.DecimalField(max_digits=300, decimal_places=150)
    m_min2 = models.DecimalField(max_digits=300, decimal_places=150)
    m_ms2 = models.DecimalField(max_digits=300, decimal_places=150)
    m_ns2 = models.DecimalField(max_digits=300, decimal_places=150)
    m_s2 = models.DecimalField(max_digits=300, decimal_places=150)
    m_us2 = models.DecimalField(max_digits=300, decimal_places=150)
    mi_h2 = models.DecimalField(max_digits=300, decimal_places=150)
    mi_min2 = models.DecimalField(max_digits=300, decimal_places=150)
    mi_ms2 = models.DecimalField(max_digits=300, decimal_places=150)
    mi_ns2 = models.DecimalField(max_digits=300, decimal_places=150)
    mi_s2 = models.DecimalField(max_digits=300, decimal_places=150)
    mi_us2 = models.DecimalField(max_digits=300, decimal_places=150)
    mm_ms2 = models.DecimalField(max_digits=300, decimal_places=150)
    mm_ns2 = models.DecimalField(max_digits=300, decimal_places=150)
    mm_s2 = models.DecimalField(max_digits=300, decimal_places=150)
    mm_us2 = models.DecimalField(max_digits=300, decimal_places=150)
    nm_ms2 = models.DecimalField(max_digits=300, decimal_places=150)
    nm_ns2 = models.DecimalField(max_digits=300, decimal_places=150)
    nm_s2 = models.DecimalField(max_digits=300, decimal_places=150)
    nm_us2 = models.DecimalField(max_digits=300, decimal_places=150)
    um_ms2 = models.DecimalField(max_digits=300, decimal_places=150)
    um_ns2 = models.DecimalField(max_digits=300, decimal_places=150)
    um_s2 = models.DecimalField(max_digits=300, decimal_places=150)
    um_us2 = models.DecimalField(max_digits=300, decimal_places=150)
    yd_min2 = models.DecimalField(max_digits=300, decimal_places=150)
    yd_ms2 = models.DecimalField(max_digits=300, decimal_places=150)
    yd_ns2 = models.DecimalField(max_digits=300, decimal_places=150)
    yd_s2 = models.DecimalField(max_digits=300, decimal_places=150)
    yd_us2 = models.DecimalField(max_digits=300, decimal_places=150)

    class Meta:
        verbose_name = 'Acceleration'
        verbose_name_plural = 'Acceleration'
        ordering = ["id"]

    def __str__(self):
        return self.unit


class Force(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit = models.CharField(max_length=100)
    attonewton = models.DecimalField(max_digits=300, decimal_places=150)
    centinewton = models.DecimalField(max_digits=300, decimal_places=150)
    decagrama_forca = models.DecimalField(max_digits=300, decimal_places=150)
    decanewton = models.DecimalField(max_digits=300, decimal_places=150)
    decigrama_forca = models.DecimalField(max_digits=300, decimal_places=150)
    decinewton = models.DecimalField(max_digits=300, decimal_places=150)
    dina = models.DecimalField(max_digits=300, decimal_places=150)
    exanewton = models.DecimalField(max_digits=300, decimal_places=150)
    femtonewton = models.DecimalField(max_digits=300, decimal_places=150)
    giganewton = models.DecimalField(max_digits=300, decimal_places=150)
    grama_forca = models.DecimalField(max_digits=300, decimal_places=150)
    hectonewton = models.DecimalField(max_digits=300, decimal_places=150)
    joule_metro = models.DecimalField(max_digits=300, decimal_places=150)
    kip = models.DecimalField(max_digits=300, decimal_places=150)
    libra_forca = models.DecimalField(max_digits=300, decimal_places=150)
    meganewton = models.DecimalField(max_digits=300, decimal_places=150)
    megapond = models.DecimalField(max_digits=300, decimal_places=150)
    micronewton = models.DecimalField(max_digits=300, decimal_places=150)
    milinewton = models.DecimalField(max_digits=300, decimal_places=150)
    nanonewton = models.DecimalField(max_digits=300, decimal_places=150)
    newton = models.DecimalField(max_digits=300, decimal_places=150)
    onca_forca = models.DecimalField(max_digits=300, decimal_places=150)
    petanewton = models.DecimalField(max_digits=300, decimal_places=150)
    piconewton = models.DecimalField(max_digits=300, decimal_places=150)
    pond = models.DecimalField(max_digits=300, decimal_places=150)
    poundal = models.DecimalField(max_digits=300, decimal_places=150)
    quilograma_forca = models.DecimalField(max_digits=300, decimal_places=150)
    quilonewton = models.DecimalField(max_digits=300, decimal_places=150)
    quilopond = models.DecimalField(max_digits=300, decimal_places=150)
    sthene = models.DecimalField(max_digits=300, decimal_places=150)
    teranewton = models.DecimalField(max_digits=300, decimal_places=150)
    tonelada_forca = models.DecimalField(max_digits=300, decimal_places=150)
    yoctonewton = models.DecimalField(max_digits=300, decimal_places=150)
    yottanewton = models.DecimalField(max_digits=300, decimal_places=150)
    zeptonewton = models.DecimalField(max_digits=300, decimal_places=150)
    zettanewton = models.DecimalField(max_digits=300, decimal_places=150)

    class Meta:
        verbose_name = 'Force'
        verbose_name_plural = 'Force'
        ordering = ["id"]

    def __str__(self):
        return self.unit


class Pressure(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit = models.CharField(max_length=100)
    atmosfera_padrao = models.DecimalField(max_digits=300, decimal_places=150)
    atmosfera_tecnico = models.DecimalField(max_digits=300, decimal_places=150)
    attobar = models.DecimalField(max_digits=300, decimal_places=150)
    attopascal = models.DecimalField(max_digits=300, decimal_places=150)
    bar = models.DecimalField(max_digits=300, decimal_places=150)
    barad = models.DecimalField(max_digits=300, decimal_places=150)
    barye = models.DecimalField(max_digits=300, decimal_places=150)
    centibar = models.DecimalField(max_digits=300, decimal_places=150)
    centihg = models.DecimalField(max_digits=300, decimal_places=150)
    centimetro_de_agua_4_C = models.DecimalField(
        max_digits=300, decimal_places=150)
    centimetro_de_mercurio_0_C = models.DecimalField(
        max_digits=300, decimal_places=150)
    centipascal = models.DecimalField(max_digits=300, decimal_places=150)
    centitorr = models.DecimalField(max_digits=300, decimal_places=150)
    coluna_de_agua_centimetro = models.DecimalField(
        max_digits=300, decimal_places=150)
    coluna_de_agua_milimetro = models.DecimalField(
        max_digits=300, decimal_places=150)
    coluna_de_agua_polegada = models.DecimalField(
        max_digits=300, decimal_places=150)
    decabar = models.DecimalField(max_digits=300, decimal_places=150)
    decapascal = models.DecimalField(max_digits=300, decimal_places=150)
    decibar = models.DecimalField(max_digits=300, decimal_places=150)
    decipascal = models.DecimalField(max_digits=300, decimal_places=150)
    decitorr = models.DecimalField(max_digits=300, decimal_places=150)
    dina_centimetro_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    exabar = models.DecimalField(max_digits=300, decimal_places=150)
    exapascal = models.DecimalField(max_digits=300, decimal_places=150)
    femtobar = models.DecimalField(max_digits=300, decimal_places=150)
    femtopascal = models.DecimalField(max_digits=300, decimal_places=150)
    gigabar = models.DecimalField(max_digits=300, decimal_places=150)
    gigapascal = models.DecimalField(max_digits=300, decimal_places=150)
    grama_forca_centimetro_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    hectobar = models.DecimalField(max_digits=300, decimal_places=150)
    hectopascal = models.DecimalField(max_digits=300, decimal_places=150)
    kip_pe_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    kip_polegada_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    libra_pe_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    libra_polegada_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    megabar = models.DecimalField(max_digits=300, decimal_places=150)
    meganewton_metro_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    megapascal = models.DecimalField(max_digits=300, decimal_places=150)
    metro_de_ar_0_C = models.DecimalField(max_digits=300, decimal_places=150)
    metro_de_ar_15_C = models.DecimalField(max_digits=300, decimal_places=150)
    microbar = models.DecimalField(max_digits=300, decimal_places=150)
    micrometro_de_agua_4_C = models.DecimalField(
        max_digits=300, decimal_places=150)
    micrometro_de_mercurio_0_C = models.DecimalField(
        max_digits=300, decimal_places=150)
    micropascal = models.DecimalField(max_digits=300, decimal_places=150)
    milibar = models.DecimalField(max_digits=300, decimal_places=150)
    milihg = models.DecimalField(max_digits=300, decimal_places=150)
    milimetro_de_agua_4_C = models.DecimalField(
        max_digits=300, decimal_places=150)
    milimetro_de_mercurio_0_C = models.DecimalField(
        max_digits=300, decimal_places=150)
    milipascal = models.DecimalField(max_digits=300, decimal_places=150)
    militorr = models.DecimalField(max_digits=300, decimal_places=150)
    nanobar = models.DecimalField(max_digits=300, decimal_places=150)
    nanopascal = models.DecimalField(max_digits=300, decimal_places=150)
    newton_metro_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    newton_milimetro_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    onca_polegada_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    pascal = models.DecimalField(max_digits=300, decimal_places=150)
    pe_de_agua_4_C = models.DecimalField(max_digits=300, decimal_places=150)
    pe_de_ar_0_C = models.DecimalField(max_digits=300, decimal_places=150)
    pe_de_ar_15_C = models.DecimalField(max_digits=300, decimal_places=150)
    pe_de_mercurio_0_C = models.DecimalField(
        max_digits=300, decimal_places=150)
    petabar = models.DecimalField(max_digits=300, decimal_places=150)
    petapascal = models.DecimalField(max_digits=300, decimal_places=150)
    picobar = models.DecimalField(max_digits=300, decimal_places=150)
    picopascal = models.DecimalField(max_digits=300, decimal_places=150)
    pieze = models.DecimalField(max_digits=300, decimal_places=150)
    polegada_de_agua_4_C = models.DecimalField(
        max_digits=300, decimal_places=150)
    polegada_de_ar_0_C = models.DecimalField(
        max_digits=300, decimal_places=150)
    polegada_de_ar_15_C = models.DecimalField(
        max_digits=300, decimal_places=150)
    polegada_de_mercurio_0_C = models.DecimalField(
        max_digits=300, decimal_places=150)
    poundal_pe_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    quilobar = models.DecimalField(max_digits=300, decimal_places=150)
    quilograma_forca_centimetro_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    quilograma_forca_metro_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    quilograma_forca_milimetro_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    quilonewton_metro_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    quilopascal = models.DecimalField(max_digits=300, decimal_places=150)
    quilopond_centimetro_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    quilopond_metro_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    quilopond_milimetro_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    sthene_metro_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    terabar = models.DecimalField(max_digits=300, decimal_places=150)
    terapascal = models.DecimalField(max_digits=300, decimal_places=150)
    tonelada_curta_pe_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    tonelada_curta_polegada_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    tonelada_longa_pe_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    tonelada_longa_polegada_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    tonelada_metro_ao_quadrado = models.DecimalField(
        max_digits=300, decimal_places=150)
    torr = models.DecimalField(max_digits=300, decimal_places=150)
    yoctobar = models.DecimalField(max_digits=300, decimal_places=150)
    yoctopascal = models.DecimalField(max_digits=300, decimal_places=150)
    yottabar = models.DecimalField(max_digits=300, decimal_places=150)
    yottapascal = models.DecimalField(max_digits=300, decimal_places=150)
    zeptobar = models.DecimalField(max_digits=300, decimal_places=150)
    zeptopascal = models.DecimalField(max_digits=300, decimal_places=150)
    zettabar = models.DecimalField(max_digits=300, decimal_places=150)
    zettapascal = models.DecimalField(max_digits=300, decimal_places=150)

    class Meta:
        verbose_name = 'Pressure'
        verbose_name_plural = 'Pressure'
        ordering = ["id"]

    def __str__(self):
        return self.unit


class Temperature(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit = models.CharField(max_length=100)
    kelvin = models.CharField(max_length=100)
    celsius = models.CharField(max_length=100)
    fahrenheit = models.CharField(max_length=100)
    rankine = models.CharField(max_length=100)
    reaumur = models.CharField(max_length=100)
    romer = models.CharField(max_length=100)
    newton = models.CharField(max_length=100)
    delisle = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Temperature'
        verbose_name_plural = 'Temperature'
        ordering = ["id"]

    def __str__(self):
        return self.unit
