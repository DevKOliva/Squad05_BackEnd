from django.contrib import admin

# Register your models here.
from .models import Profissional, Card_Conteudo

admin.site.register(Profissional)
admin.site.register(Card_Conteudo)