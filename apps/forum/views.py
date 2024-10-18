from django.shortcuts import render
from .models import Topico, Comentario

def forum(request):
    return render(request, 'forum.html')

# Create your views here.
def index(request):

    topicos = Topico.objects.all()
    comentarios = Comentario.objects.all()

    context = {
        'topicos': topicos,
        'comentarios': comentarios,
    }

    return render(request, 'forum.html', context)
