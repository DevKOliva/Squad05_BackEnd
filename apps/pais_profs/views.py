from django.shortcuts import render
from .models import Descricao, Categoria, Card


def pais_profs(request):
    
    descricao = Descricao.objects.all()
    categoria = Categoria.objects.all()
    card = Card.objects.all()

    dados = []

    for i in categoria:
        dici = {
            'categoria': i,
            'card':[]
        }
        for j in card:
            if j.categoria.palavraDestaque == i.palavraDestaque:
                dici['card'].append(j)
        dados.append(dici)

    context = {
        'categoria' : categoria,
        'card' : card,
        'descricao' : descricao,
        'dados' : dados,
    }

    return render(request, 'pais_profs.html', context)

