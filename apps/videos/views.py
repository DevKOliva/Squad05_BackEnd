from django.shortcuts import render
from .models import Categoria, Video, Descricao


def videos(request):
    
    categoria = Categoria.objects.all()
    video = Video.objects.all()

    context = {
        'categoria' : categoria,
        'video' : video,
    }

    return render(request,'videos.html',context)

