from django.shortcuts import render
from .models import Categoria, Video


def videos(request):
    
    categoria = Categoria.objects.all()
    video = Video.objects.all()

    dados = []


    for i in categoria:
        dici = {
            'categoria': i,
            'video':[]
        }
        for j in video:
            if j.categoria.palavraDestaque == i.palavraDestaque:
                dici['video'].append(j)
        dados.append(dici)

    context = {
        'categoria' : categoria,
        'video' : video,
        'dados' : dados,
    }

    return render(request,'videos.html',context)

