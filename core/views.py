from django.shortcuts import render
from .models import *
# Create your views here.
def indexx(request):
    moshinas = Moshina.objects.all()
    context = {
        'moshinas': moshinas
    }
    return render(request, 'index.html', context)