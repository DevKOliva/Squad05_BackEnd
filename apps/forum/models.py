import datetime
from django.db import models

# Create your models here.
class Topico(models.Model):
    titulo = models.CharField(verbose_name='Nome do topico', default='', null=False, max_length=50)
    descricao = models.CharField(verbose_name='Descrição do topico', default='', null=False, max_length=100)
    pessoas_discutindo = models.IntegerField(verbose_name='Pessoas discutindo', default=0, null=False)
    criado_a = models.IntegerField(verbose_name='Criado a', default = 0, null=False)

    def __str__(self):
        return str(self.id)
    
class Comentario(models.Model):
    nome_usuario = models.CharField(verbose_name='Nome do usuário', default='', null=False, max_length=50)
    titulo = models.CharField(verbose_name='Título do comentário', default='', null=False, max_length=50)
    comentario = models.CharField(verbose_name='Comentário do usuário', default='', null=False, max_length=300)
    pessoas_comentando = models.IntegerField(verbose_name='Pessoas comentando', default=0, null=False)
    favoritado = models.BooleanField(verbose_name='Favoritado', null=False)
    criado_a = models.IntegerField(verbose_name='Criado a', default = 0, null=False)

    def __str__(self):
        return str(self.id)