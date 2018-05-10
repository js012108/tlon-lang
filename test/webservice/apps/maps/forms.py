from .models import *
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('temp','hum','longitud','latitud','humsuelo','precipitacion',)
        labels = {"temp":"Temperatura", "hum":"Humedad Relativa","humsuelo":"Humedad Suelo","precipitacion":"Precipitación"}

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ('onelat','onelong','twolat','twolong','threelat','threelong','fourlat','fourlong','datecrop','crop',)
        labels = {"onelat":"Latitud 1", "onelong":"Longitud 1","twolat":"Latitud 2","twolong":"Longitud 2","threelat":"Latitud 3","threelong":"Longitud 3","fourlat":"Latitud 4","fourlong":"Longitud 4","crop":"Cultivo","datecrop":"Días de sembrado"}

class GroundForm(forms.ModelForm):
    class Meta:
        model = Ground
        fields = {'ground1','ground2','ground3','crop','cmg1','cmg2','cmg3',}
        labels = {"ground2":"Suelo 2","ground3":"Suelo 3","cmg1":"Medida Suelo 1 (cm)","cmg2":"Medida Suelo 2 (cm)","cmg3":"Medida Suelo 3 (cm)","crop": "Cultivo","ground1":"Suelo 1"}
