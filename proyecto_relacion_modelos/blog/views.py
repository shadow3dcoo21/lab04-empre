from django.shortcuts import render
from .models import Entrada

def lista_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'blog/lista_entradas.html', {'entradas': entradas})

# Create your views here.
