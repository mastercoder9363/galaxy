from django.shortcuts import render
from .models import *
# Create your views here.
from django.views.generic import  *
def indexx(request):
    moshinas = Moshina.objects.all()
    sos = SO.objects.all()  
    context = {
        'moshinas': moshinas,
        'sos': sos
    }
    return render(request, 'index.html', context)
def malibuu(request):
    return render(request, 'malibu.html')


class AboutView(TemplateView):
    template_name ='about.html'