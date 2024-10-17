from django.db import models

class Descricao(models.Model):
    titulo = models.CharField(verbose_name='escreva o titulo sem as palavras destacadas', max_length=100)
    primeiraDestaque = models.CharField(verbose_name='escreva a primeira palavra destacada', max_length=50)
    segundaDestaque = models.CharField(verbose_name='escreva a segunda palavra destacada', max_length=50)
    terceiraDestaque = models.CharField(verbose_name='escreva a terceira palavra destacada', max_length=50)
    descricao = models.TextField(verbose_name='escreva a descrição')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
class Textinho(models.Model):
    textinho = models.TextField(verbose_name='escreva o textinho')
    img1 = models.ImageField(upload_to='fotos/%d/%m/%Y')
    img2 = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

class Categoria(models.Model):
    nome = models.CharField(verbose_name='escreva a categoria', max_length=100)
    palavraDestaque = models.CharField(verbose_name='escreva a palavra destaque', max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome


class Video(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    video = models.ImageField(upload_to='fotos/%d/%m/%Y')
    nomevideo = models.CharField(verbose_name='qual o nome do card', default='', max_length=50, null= False)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomevideo