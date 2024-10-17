from django.db import models

class Descricao(models.Model):
    titulo = models.CharField(verbose_name='escreva a descrição', max_length=100)
    palavraDestaqueUm = models.CharField(verbose_name='primeira palavra destaque', max_length=50)
    palavraDestaqueDois = models.CharField(verbose_name='primeira segunda destaque', max_length=50)
    descricao = models.TextField(verbose_name='')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nome = models.CharField(verbose_name='escreva a categoria', max_length=100)
    palavraDestaque = models.CharField(verbose_name='escreva a palavra destaque', max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome

class Card(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='fotos/%d/%m/%Y')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.categoria
