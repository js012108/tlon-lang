from django.views.generic import TemplateView
from django.shortcuts import render

class Index(TemplateView):
    template_name = 'index/index.html'

    def get(self, request):
        context = {
            'header': {
                'title': 'Inicio',
                'subtitle': '',
                'breadcrumb': [
                    { 'name': 'Inicio' }
                ],
                'options': [],
            }
        }
        return render(request, self.template_name, context)

class Index2(TemplateView):
    template_name = 'index/index2.html'

    def get(self, request):
        context = {
            'header': {
                'title': 'Inicio',
                'subtitle': '',
                'breadcrumb': [
                    { 'name': 'Inicio' }
                ],
                'options': [],
            }
        }
        return render(request, self.template_name, context)
    
class Login(TemplateView):
    template_name = 'index/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self,request):
        print(request.POST['temp'])
        return render(request, self.template_name)
