from django.db import models

# Create your models here.
class Card_Conteudo(models.Model):
    titulo = models.CharField(verbose_name='Nome do card', blank=True, null=True, max_length=50)
    palavra_destaque = models.CharField(verbose_name='Palavra de destaque', blank=True, null=True, max_length=50)
    descricao = models.CharField(verbose_name='Descrição do card', max_length=50)
    categoria = models.CharField(verbose_name='Categoria do card', max_length=20)
    foto_card = models.ImageField(upload_to='foto_card/%d/%m%Y', default='core/static/imagem_padrao/padrao.jpg', blank=True, null=True)

    def __str__(self):
        return str(self.id)

class Profissional(models.Model):
    nome = models.CharField(verbose_name='Nome do profissional', null = False, max_length=100)
    profissao = models.CharField(verbose_name='Nome da profissão', null = False, max_length=50)
    identidade_profissional = models.CharField(verbose_name='Carteira de Identidade Profissional', default='', blank=True, null=True, max_length=50)
    foto_profissional = models.ImageField(upload_to='foto/%d/%m%Y', default='core/static/imagem_padrao/padrao.jpg', null = False)

    def __str__(self):
        return self.nome