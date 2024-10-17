from django.db import models

class Colorir(models.Model):
    titulo = models.CharField(verbose_name='Digite o nome', max_length=50)
    card = models.ImageField(upload_to='fotos/%d/%m/%Y')

class Didatico(models.Model):
    titulo = models.CharField(verbose_name='qual a materia', max_length=50)
    card = models.ImageField(upload_to='fotos/%d/%m/%Y')

class Pais_profs(models.Model):
    titulo = models.CharField(verbose_nome='Lorem ipsum', max_length=50)
    card = models.ImageField(upload_to='fotos/%d/%m/%Y')




