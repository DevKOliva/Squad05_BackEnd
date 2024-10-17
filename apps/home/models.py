from django.db import models

class Ferramenta(models.Model):
    nome = models.CharField(verbose_name='Nome da ferramenta', max_length=50)
    descricao = models.CharField(verbose_name='Descrição da ferramenta', max_length=50)

class Profissional(models.Model):
    nome = models.CharField(verbose_name='Nome do profissional', max_length=100)
    profissao = models.CharField(verbose_name='Nome da profissão', max_length=50)
