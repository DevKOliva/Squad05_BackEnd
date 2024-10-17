# Generated by Django 5.1.2 on 2024-10-15 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ferramenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome da ferramenta')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição da ferramenta')),
            ],
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do profissional')),
                ('profissao', models.CharField(max_length=50, verbose_name='Nome da profissão')),
            ],
        ),
    ]
