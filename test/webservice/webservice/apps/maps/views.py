from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.utils.timezone import now
import datetime
from django.db.models import Avg, Max, Min, Sum

@method_decorator(csrf_exempt, name='dispatch')
class Map(TemplateView):
    template_name = 'maps/map.html'

    def get(self, request):
        context = {
            'header': {
                'title': 'Inicio',
                'subtitle': '',
                'breadcrumb': [
                    { 'name': 'Inicio' }
                ],
                'options': [],
            },
            'datos':Data.objects.all()
        }
        return render(request, self.template_name, context)

    def post(self,request):
        temp = request.POST['temp']
        hum = request.POST['hum']
        longitud = request.POST['longitud']
        latitud = request.POST['latitud']
        humsuelo = request.POST['humsuelo']
        precipitacion = request.POST['precipitacion']
        datemed = request.POST['datemed']
        data = Data(temp = temp, hum = hum, latitud = latitud, longitud = longitud, humsuelo = humsuelo, precipitacion = precipitacion, datemed = datemed)
        data.save()
        return render(request, self.template_name)

class Create_measurement(TemplateView):
    template_name = 'maps/create_measurement.html'

    def get(self, request):
        context = {
            'header': {
                'title': 'Crear Medida',
                'subtitle': '',
                'breadcrumb': [
                    { 'name': 'Inicio' }
                ],
                'options': [],
            },
            'form': DataForm
        }
        return render(request, self.template_name, context)

    def post(self,request):
        form = DataForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('maps:create_measurement')
        return redirect('maps:create_measurement')

class Crops(TemplateView):
    template_name = 'maps/crops.html'

    def get(self, request):
        context = {
            'header': {
                'title': 'Cultivos',
                'subtitle': '',
                'breadcrumb': [
                    { 'name': 'Inicio' }
                ],
                'options': [],
            },
            'form': CropForm
        }
        return render(request, self.template_name, context)
    def post(self,request):
        form = CropForm(request.POST)
        if form.is_valid():
            crop = form.save(commit=False)
            if(crop.crop==1 or crop.crop==2):
                crop.pre = 75
            else:
                crop.pre = (30*0.75)
            crop.save()
            return redirect('maps:ground')
        return redirect('maps:crops')


class Grounds(TemplateView):
    template_name = 'maps/ground.html'

    def get(self, request):
        context = {
            'header': {
                'title': 'Cultivos',
                'subtitle': '',
                'breadcrumb': [
                    { 'name': 'Inicio' }
                ],
                'options': [],
            },
            'form': GroundForm
        }
        return render(request, self.template_name, context)
    def post(self,request):
        form = GroundForm(request.POST)
        if form.is_valid():
            ground = form.save(commit=False)
            aux = 0
            aux += (ground.ground1*ground.cmg1) / 100
            aux += (ground.ground2*ground.cmg2) / 100
            aux += (ground.ground3*ground.cmg3) / 100
            ground.laa = aux
            ground.lac = aux
            ground.save()
            return redirect('maps:irrigation')
        return redirect('index:menu')

class Irrigations(TemplateView):
    template_name = 'maps/irrigation.html'
    context = {
        'header': {
            'title': 'Riego',
            'subtitle': '',
            'breadcrumb': [
                { 'name': 'Inicio' }
            ],
            'options': [],
        }
    }

    def get(self, request):
        if(Irrigation.objects.all().count()>0):
            lastirrigat = Irrigation.objects.all().last()
            if(lastirrigat.dateprocess.day==now().day and lastirrigat.dateprocess.month==now().month and lastirrigat.dateprocess.year==now().year):
                self.context['message']='El riego sugerido de hoy ya fue calculado.'
                self.context['lac'] = lastirrigat.ground.lac
                self.context['laa'] = lastirrigat.ground.laa
                if 'message2' in self.context:
                    del self.context['message2']
                if 'alert' in self.context:
                    del self.context['alert']
                if 'irrigat' in self.context:
                    del self.context['irrigat']
                if 'eto' in self.context:
                    del self.context['eto']
            else:
                self.context['message']='El riego sugerido de hoy se ha empezado a calcular.'
                radiation=[34.6, 36.4, 37.6, 37.4, 36.0, 35.0, 35.3, 36.5, 37.3, 36.6, 34.9, 33.9]
                temp_avg = Data.objects.aggregate(Avg('temp'))['temp__avg']
                prec_sum = Data.objects.aggregate(Sum('precipitacion'))['precipitacion__sum']
                temp_max = Data.objects.aggregate(Max('temp'))['temp__max']
                temp_min = Data.objects.aggregate(Min('temp'))['temp__min']
                lastirrigat.eto = 0.0023*(temp_avg+17.78)*radiation[now().month-1]*((temp_max-temp_min)**(0.5))
                self.context['eto'] = lastirrigat.eto
                papadur = [25,55,100,130]
                papak = [0.5,0.5,1.15,0.75]
                maizdur = [20,45,70,80]
                maizk = [0.3, 0.3, 1.15, 0.75]
                cebolladur = [20,65,85,95]
                cebollak = [0.7,0.7,1,1]
                lastirrigat.precefec = prec_sum
                k=0
                if(lastirrigat.ground.crop.crop==1):
                    k = maizk[0]
                    for i in range(len(maizdur)):
                        if lastirrigat.ground.crop.datecrop>=maizdur[i]:
                            k = maizk[i]
                    print(k)
                elif(lastirrigat.ground.crop.crop==2):
                    k = papak[0]
                    for i in range(len(papadur)):
                        if lastirrigat.ground.crop.datecrop>=papadur[i]:
                            k = papak[i]
                    print(k)
                elif(lastirrigat.ground.crop.crop==3):
                    k = cebollak[0]
                    for i in range(len(cebolladur)):
                        if lastirrigat.ground.crop.datecrop>=cebolladur[i]:
                            k = cebollak[i]
                    print(k)
                ett = k*lastirrigat.eto
                laatoday = lastirrigat.ground.lac-ett+lastirrigat.precefec
                if(laatoday<lastirrigat.ground.laa):
                    lastirrigat.ground.lac = laatoday
                    self.context['message2'] = "La lamina de agua ha disminuido"
                    if(laatoday<=lastirrigat.ground.laa/2):
                        self.context['alert'] = "ALERTA!!! ES NECESARIO REGAR EL CULTIVO."
                        self.context['irrigat'] = lastirrigat.ground.laa - laatoday
                        #lastirrigat.ground.lac = lastirrigat.ground.laa
                lastirrigat.ground.save()
                self.context['lac'] = laatoday
                self.context['laa'] = lastirrigat.ground.laa
                #lastirrigat.dateprocess = now()
                lastirrigat.save()
        else:
            if(Ground.objects.all().count()>0):
                ground = Ground.objects.all().last()
                irrigat = Irrigation(eto=0,precefec=0,ground=ground)
                irrigat.save()


        return render(request, self.template_name, self.context)

class Massive_upload(TemplateView):
    template_name = 'maps/massive_upload.html'

    def get(self, request):
        return render(request, self.template_name)


class Support(TemplateView):
    template_name = 'maps/support.html'

    def get(self, request):
        return render(request, self.template_name)


class Measurement(TemplateView):
    template_name = 'maps/measurement.html'

    def get(self, request):
        context = {
            'header': {
                'title': 'Tabla de Medidas',
                'subtitle': '',
                'breadcrumb': [
                    { 'name': 'Inicio' }
                ],
                'options': [],
            },
            'medidas': Data.objects.all()
        }
        return render(request, self.template_name, context)
