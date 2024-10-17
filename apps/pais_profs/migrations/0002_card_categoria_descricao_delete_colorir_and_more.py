# Generated by Django 5.1.2 on 2024-10-17 02:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pais_profs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='fotos/%d/%m/%Y')),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='escreva a categoria')),
                ('palavraDestaque', models.CharField(max_length=50, verbose_name='escreva a categoria')),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Descricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='escreva a descrição')),
                ('palavraDestaqueUm', models.CharField(max_length=50, verbose_name='primeira palavra destaque')),
                ('palavraDestaqueDois', models.CharField(max_length=50, verbose_name='primeira segunda destaque')),
                ('descricao', models.TextField(verbose_name='')),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Colorir',
        ),
        migrations.DeleteModel(
            name='Didatico',
        ),
        migrations.DeleteModel(
            name='Pais_profs',
        ),
        migrations.AddField(
            model_name='card',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pais_profs.categoria'),
        ),
    ]