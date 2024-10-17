# Generated by Django 5.1.2 on 2024-10-17 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pais_profs', '0002_card_categoria_descricao_delete_colorir_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='palavraDestaque',
            field=models.CharField(max_length=50, verbose_name='escreva a palavra destaque'),
        ),
        migrations.AlterField(
            model_name='descricao',
            name='descricao',
            field=models.TextField(verbose_name='escreva a descrição'),
        ),
        migrations.AlterField(
            model_name='descricao',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='escreva o titulo'),
        ),
    ]