from django.shortcuts import render
from .models import Profissional, Card_Conteudo

# Create your views here.
def index(request):

    profissionais = Profissional.objects.all()

    cards_conteudo = Card_Conteudo.objects.all()

    context = {
        'profissionais': profissionais,
        'cards_conteudo': cards_conteudo, 
    }

    return render(request, 'index.html', context)