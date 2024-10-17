from django.shortcuts import render
from .models import Descricao, Categoria, Card


def pais_profs(request):
    
    descricao = Descricao.objects.all()
    categoria = Categoria.objects.all()
    card = Card.objects.all()

    card1 = Card.objects.filter(categoria__palavraDestaque='Colorir')

    context = {
        'categoria' : categoria,
        'card' : card,
        'descricao' : descricao,
        'card1' : card1,
    }

    return render(request, 'pais_profs.html', context)

