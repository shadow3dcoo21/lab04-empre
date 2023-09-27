from django.shortcuts import render


from django.shortcuts import render, get_object_or_404
from .models import Autor, Entrada

def pagina_inicio(request):
    autores = Autor.objects.all()
    return render(request, 'pagina_inicio.html', {'autores': autores})

def entradas_por_autor(request, id_autor):
    autor = get_object_or_404(Autor, pk=id_autor)
    entradas = Entrada.objects.filter(autor=autor)
    return render(request, 'entradas_por_autor.html', {'autor': autor, 'entradas': entradas})

# Create your views here.
