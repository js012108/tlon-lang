from django.db import models
from django.utils.timezone import now

class Data(models.Model):
    temp = models.FloatField(default=0,)
    hum = models.FloatField(default=0,blank=True)
    longitud = models.FloatField()
    latitud = models.FloatField()
    humsuelo = models.FloatField(default=0,blank=True)
    precipitacion = models.FloatField(default=0,blank=True)
    datemed = models.DateTimeField(blank=True,default=now)
    def __str__(self):
        return '%f %f %s' % (self.longitud,self.latitud,self.datemed)

class Crop(models.Model):
    CROPS = (
        (1, 'Maiz'),
        (2, 'Papa'),
        (3, 'Cebolla'),
    )
    crop = models.IntegerField(choices=CROPS)
    onelat = models.FloatField()
    onelong = models.FloatField()
    twolat = models.FloatField()
    twolong = models.FloatField()
    threelat = models.FloatField()
    threelong = models.FloatField()
    fourlat = models.FloatField()
    fourlong = models.FloatField()
    pre = models.FloatField()
    datecrop = models.IntegerField()
    def __str__(self):
        return '%s (%f cm)' % (self.CROPS[self.crop-1][1],self.pre)

class Ground(models.Model):
    GROUNDS = (
        (9, 'Arenoso'),
        (13, 'Franco Arenoso'),
        (17, 'Franco'),
        (20, 'Franco Arcilloso'),
        (21, 'Arcillo-arenoso'),
        (23, 'Arcilloso'),
    )
    ground1 = models.IntegerField(choices=GROUNDS)
    cmg1 = models.FloatField()
    ground2 = models.IntegerField(choices=GROUNDS)
    cmg2 = models.FloatField()
    ground3 = models.IntegerField(choices=GROUNDS)
    cmg3 = models.FloatField()
    laa = models.FloatField()
    lac = models.FloatField()
    crop = models.OneToOneField(Crop,on_delete=models.CASCADE,primary_key=True,)

    def __str__(self):
        return '%s %f %f' % (self.crop, self.laa, self.lac)

class Irrigation(models.Model):
    eto = models.FloatField()
    ground = models.OneToOneField(Ground,on_delete=models.CASCADE,primary_key=True,)
    precefec = models.FloatField()
    dateprocess = models.DateTimeField(blank=True,default=now)
    def __str__(self):
        return '%s ' % (self.ground)

class MigracionBaseCertificada(models.Model):
    file_url = models.CharField(max_length=100)
    fecha_migracion = models.DateTimeField(default=None, blank=True, null=True)
    id_usuario_creado = models.CharField(max_length=100)
    id_usuario_ejecuto = models.CharField(max_length=100, default=None, blank=True, null=True)
    fecha_creacion = models.DateTimeField(null=True)


class UsuarioSisben (models.Model):
    TIPOS_DOCUMENTO = (
        (0, 'No tiene'),
        (1, 'Cédula de ciudadanía'),
        (2, 'Tarjeta de identidad'),
        (3, 'Cédula de extranjería'),
        (4, 'Registro civil')
    )

    GENEROS = (
        (1, 'Masculino'),
        (2, 'Femenino')
    )

    ESTADOS_CIVILES = (
        (1, 'Unión libre'),
        (2, 'Casado'),
        (3, 'Viudo'),
        (4, 'Separado o divorciado'),
        (5, 'Soltero'),
    )

    PAISES = (
        (1, 'COLOMBIA'),
        (2, 'VENEZUELA')
    )

    DEPARTAMENTOS = (
        (1, 'AMAZONAS'),
        (2, 'ANTIOQUIA'),
        (3, 'ARAUCA'),
        (4, 'ATLÁNTICO'),
        (5, 'BOLÍVAR'),
        (6, 'BOYACÁ'),
        (7, 'CALDAS'),
        (8, 'CAQUETÁ'),
        (9, 'CASANARE'),
        (10, 'CAUCA'),
        (11, 'CESAR'),
        (12, 'CHOCÓ'),
        (13, 'CÓRDOBA'),
        (14, 'CUNDINAMARCA'),
        (15, 'GUAINIA'),
        (16, 'GUAVIARE'),
        (17, 'HUILA'),
        (18, 'LA GUAJIRA'),
        (19, 'MAGDALENA'),
        (20, 'META'),
        (21, 'NARIÑO'),
        (22, 'NORTE DE SANTANDER'),
        (23, 'PUTUMAYO'),
        (24, 'QUINDÍO'),
        (25, 'RISARALDA'),
        (26, 'SAN ANDRES Y PROVIDENCIA'),
        (27, 'SANTANDER'),
        (28, 'SUCRE'),
        (29, 'TOLIMA'),
        (30, 'VALLE DEL CAUCA'),
        (31, 'VAUPES'),
        (32, 'VICHADA')
    )

    MUNICIPIOS = (
        (1, 'ARAUCA'),
        (2, 'ARAUQUITA'),
        (3, 'CRAVO NORTE'),
        (4, 'FORTUL'),
        (5, 'PUERTO RONDON'),
        (6, 'SARAVENA'),
        (7, 'TAME')
    )

    BARRIOS = (
        (1, '1 DE ENERO'),
        (2, '1 DE MAYO'),
        (3, '12 DE OCTUBRE'),
        (4, '20 DE JULIO'),
        (5, '7 DE AGOSTO'),
        (6, 'BARRIO VILLA LUZ'),
        (7, 'BRISAS DEL ARAUCA'),
        (8, 'BRISAS DEL LLANO '),
        (9, 'BRISAS DEL PUENTE'),
        (10, 'BUENA VISTA'),
        (11, 'BULEVAR DE LA CEIBA'),
        (12, 'CAÑAS BRAVAS'),
        (13, 'CABAÑAS DEL RIO'),
        (14, 'CARACOL'),
        (15, 'CORDOBA'),
        (16, 'COROCORAS'),
        (17, 'COSTA HERMOSA'),
        (18, 'CRISTO REY'),
        (19, 'DIVINO NIÑO'),
        (20, 'EL BOSQUE '),
        (21, 'EL CHIRCAL'),
        (22, 'EL PARAISO'),
        (23, 'EL PORVENIR'),
        (24, 'EL TRIUNFO'),
        (25, 'FLOR DE MILLANO'),
        (26, 'FUNDADORES'),
        (27, 'GUARATAROS'),
        (28, 'LA ESPERANZA'),
        (29, 'LA GRANJA'),
        (30, 'LA VICTORIA'),
        (31, 'LAS AMERICAS'),
        (32, 'LAS CHORRERAS'),
        (33, 'LIBERTADORES'),
        (34, 'MAPORILLAL'),
        (35, 'MATE VENADO'),
        (36, 'MERIDIANO 70'),
        (37, 'MIRAMAR'),
        (38, 'MIRAMAR FRONTERAS'),
        (39, 'OHITIES'),
        (40, 'OLIMPICO'),
        (41, 'PEDRO NEL JIMENEZ'),
        (42, 'SAN ANTONIO'),
        (43, 'SAN CARLOS'),
        (44, 'SAN LUIS'),
        (45, 'SANTA BARBARA'),
        (46, 'SANTA FE'),
        (47, 'SANTA FESITO'),
        (48, 'SANTA TERESITA'),
        (49, 'TODO LOS SANTOS'),
        (50, 'UNION'),
        (51, 'URBANIZACION ALTOS DE LA SABANA'),
        (52, 'URBANIZACION PARQUE CAMPESTRE'),
        (53, 'URBANIZACION ARAGUANEY'),
        (54, 'URBANIZACION ARAUCAIMA'),
        (55, 'URBANIZACION BOSQUE CLUB'),
        (56, 'URBANIZACION CEDEÑO'),
        (57, 'URBANIZACION EL ARAUCO'),
        (58, 'URBANIZACION EL HORCON'),
        (59, 'URBANIZACION EL MORICHE'),
        (60, 'URBANIZACION EL PALMAR'),
        (61, 'URBANIZACION EL PARAISO'),
        (62, 'URBANIZACION EL RODEO'),
        (63, 'URBANIZACION FLOR AMARILLO'),
        (64, 'URBANIZACION GUAYACAN'),
        (65, 'URBANIZACION LAS PLAMERAS'),
        (66, 'URBANIZACION LOS CENTAUROS'),
        (67, 'URBANIZACION PALMA REAL'),
        (68, 'URBANIZACION SANTA BARBARA'),
        (69, 'URBANIZACION VILLA DEL MAESTRO'),
        (70, 'URBANIZACION VILLA DEL PRADO'),
        (71, 'URBANIZACION CIUDAD JARDIN'),
        (72, 'URBANIZACION LA CAYENA'),
        (73, 'URBANIZACION LOS ALMENDROS'),
        (74, 'URBANIZACION MATAGEA'),
        (75, 'URBANIZACION SABANALES'),
        (76, 'URBANIZACION VILLA CELESTE'),
        (77, 'VILLA CECILIA'),
        (78, 'VILLA ESPERANZA'),
        (79, 'VILLA MARIA'),
        (80, 'VILLA SAN JUAN')
    )

    VEREDAS = (
        (1, 'LA MAPORITA'),
        (2, 'CABUYARE'),
        (3, 'FELICIANO'),
        (4, 'BOGOTA'),
        (5, 'LA PANCHERA'),
        (6, 'CARACOL'),
        (7, 'BARRANCA AMARILLA'),
        (8, 'PTO COLOMBIA'),
        (9, 'EL PELIGRO'),
        (10, 'PUNTO FIJO'),
        (11, 'EL VAPOR'),
        (12, 'EL MIEDO'),
        (13, 'VILLANUEVA'),
        (14, 'ELE PEROCERO'),
        (15, 'SAN PABLO'),
        (16, 'LAS MONAS'),
        (17, 'MAPORILLAL'),
        (18, 'SAN RAMON'),
        (19, 'EL SOCORRO'),
        (20, 'MERECURE'),
        (21, 'LA BENDICION'),
        (22, 'MATAL DE FLOR AMARILLO'),
        (23, 'LOS MEDANOS'),
        (24, 'LAS PLUMAS'),
        (25, 'LOS ANDES'),
        (26, 'CINARUCO'),
        (27, 'CAÑO AZUL'),
        (28, 'BOCAS DE ELE'),
        (29, 'CAÑO SECO'),
        (30, 'CAÑO COLORADO'),
        (31, 'EL VIGIA'),
        (32, 'LAURELES'),
        (33, 'LA CONQUISTA'),
        (34, 'MANANTIALES'),
        (35, 'SAN JOSE DEL LIPA'),
        (36, 'SELVAS DEL LIPA'),
        (37, 'SALTO DEL LIPA'),
        (38, 'MAPORAL'),
        (39, 'CAÑO SALAS'),
        (40, 'LA PASTORA'),
        (41, 'LA COMUNIDAD'),
        (42, 'ALTO PRIMORES'),
        (43, 'BRISAS DEL SALTO'),
        (44, 'LAS NUBES A'),
        (45, 'LAS NUBES B'),
        (46, 'EL SINAI'),
        (47, 'EL FINAL'),
        (48, 'ALTAMIRA'),
        (49, 'TODOS LOS SANTOS'),
        (50, 'LA BECERRA'),
        (51, 'CLARINETERO'),
        (52, 'MONSERRATE'),
        (53, 'ARRECIFES'),
        (54, 'MATEPIÑA'),
        (55, 'BARRANCONES'),
        (56, 'EL TORNO'),
        (57, 'LA PAYARA'),
        (58, 'MATA DE GALLINA'),
        (59, 'CHAPARRITO'),
        (60, 'EL ROSARIO'),
        (61, 'LA SAYA'),
        (62, 'COROCITO'),
        (63, 'BOCAS DEL ARAUCA'),
        (64, 'LOS CABALLOS'),
        (65, 'LLANO ALTO'),
        (66, 'LAS PLAYITAS'),
        (67, 'BRISAS DEL ARAUCA'),
        (68, 'MATA DE VENADO')
    )

    ZONAS = (
        (1, 'CABECERA'),
        (2, 'CENTRO POBLADO'),
        (3, 'RURAL DISPERSO')
    )

    ZONAS_SISBEN = (
        (1, 'RURAL'),
        (2, 'URBANA'),
        (3, 'CENTRO POBLADO')
    )

    CORREGIMIENTOS = (
        (1, 'CARACOL'),
        (2, 'MAPORILLAL'),
        (3, 'CAÑAS BRAVAS'),
        (4, 'TODOS LOS SANTOS'),
        (5, 'SANTA BARBARA')
    )

    COMUNAS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )

    PARENTESCOS = (
        (1, 'Jefe'),
        (2, 'Cónyuge o compañera(o)'),
        (3, 'Hijos'),
        (4, 'Nietos'),
        (5, 'Padres'),
        (6, 'Hermanos'),
        (7, 'Yerno o Nuera'),
        (8, 'Abuelos'),
        (9, 'Suegros'),
        (10, 'Tios'),
        (11, 'Sobrinos'),
        (12, 'Primos'),
        (13, 'Cuñados'),
        (14, 'Otros Parientes'),
        (15, 'No parientes'),
        (16, 'Servicio doméstico o cuidandero'),
        (17, 'Pariente servicio doméstico o cuidandero')
    )

    EXTRANJEROS = (
        (1, 'Si'),
        (2, 'No')
    )

    TIPOS_VIVIENDA = (
        (1, 'Casa o apartamento'),
        (2, 'Cuarto'),
        (3, 'Otro tipo de unidad de vivienda'),
        (4, 'Casa indígena')
    )

    NIVELES_EDUCATIVOS = (
        (1, 'Ninguno'),
        (2, 'Básica primaria'),
        (3, 'Básica secundaria'),
        (4, 'Técnica o tecnológica'),
        (5, 'Universidad'),
        (6, 'Postgrado')
    )

    TIPOS_ESTABLECIMIENTO = (
        (0, 'Ninguno'),
        (1, 'Centros de atención u hogares ICBF'),
        (2, 'Guardería, salacuna, preescolar, jardín, infantil público'),
        (3, 'Guardería, salacuna, preescolar, jardín infantil privado'),
        (4, 'Escuela, colegio, técnico universitario o universidad pública'),
        (5, 'Escuela, colegio, técnico universitario o universidad privada'),
        (6, 'SENA'),
        (7, 'Secundaria técnica pública'),
        (8, 'Secundaria técnica privada')
    )

    ACTIVIDADES_ECONOMICAS = (
	    (0, 'Sin Actividad'),
	    (1, 'Trabajando'),
	    (2, 'Buscando trabajo'),
	    (3, 'Estudiando'),
	    (4, 'Oficios del hogar'),
	    (5, 'Rentista'),
	    (6, 'Jubilado, pensionado'),
	    (7, 'Inválido')
    )

    # Model Attributes
    numero_registro = models.IntegerField()                                     # A
    documento_identidad = models.BigIntegerField(primary_key=True)              # BY
    tipo_documento = models.IntegerField(choices=TIPOS_DOCUMENTO)               # BX

    primer_apellido = models.CharField(max_length=100)                          # BR
    segundo_apellido = models.CharField(max_length=100, blank=True, null=True)  # BS
    primer_nombre = models.CharField(max_length=100)                            # BT
    segundo_nombre = models.CharField(max_length=100, blank=True, null=True)    # BU

    genero = models.IntegerField(choices=GENEROS)                 # BV
    fecha_nacimiento = models.DateField()                         # BZ
    edad_corte = models.IntegerField()                            # CT
    estado_civil = models.IntegerField(choices=ESTADOS_CIVILES)   # CB

    parentesco = models.IntegerField(choices=PARENTESCOS)         # CA
    extranjero = models.IntegerField(choices=EXTRANJEROS)         # BW
    ficha = models.IntegerField()                                 # B
    puntaje_sisben = models.FloatField()                          # DN
    departamento = models.IntegerField(choices=DEPARTAMENTOS)     # C
    municipio = models.IntegerField(choices=MUNICIPIOS)           # D
    zona = models.IntegerField(choices=ZONAS)                     # E
    sector = models.CharField(max_length=100)                     # F
    manzana = models.CharField(max_length=100)                    # H
    comuna = models.IntegerField(choices=COMUNAS)                 # I
    barrio = models.IntegerField(choices=BARRIOS)                 # J
    vereda = models.IntegerField(choices=VEREDAS)                 # K
    direccion = models.CharField(max_length=100)                  # L
    telefono = models.CharField(max_length=100)                   # T
    tipo_vivienda = models.IntegerField(choices=TIPOS_VIVIENDA)   # N
    estrato = models.IntegerField()                               # W
    nivel_educativo = models.IntegerField(choices=NIVELES_EDUCATIVOS)  # CM
    tipo_establecimiento = models.IntegerField(choices=TIPOS_ESTABLECIMIENTO) #CK
    actividad_economica = models.IntegerField(choices=ACTIVIDADES_ECONOMICAS) # CN
    activo = models.BooleanField(default=True)
    afrodescendiente = models.BooleanField(default=False)
