from django.contrib import admin

# Register your models here.
from .models import Topico, Comentario

admin.site.register(Topico)
admin.site.register(Comentario)