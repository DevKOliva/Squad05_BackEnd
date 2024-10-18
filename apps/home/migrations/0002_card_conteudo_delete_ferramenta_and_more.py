# Generated by Django 5.1.2 on 2024-10-18 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card_Conteudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome do card')),
                ('palavra_destaque', models.CharField(blank=True, max_length=50, null=True, verbose_name='Palavra de destaque')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição do card')),
                ('categoria', models.CharField(max_length=20, verbose_name='Categoria do card')),
                ('foto_card', models.ImageField(blank=True, default='core/static/imagem_padrao/padrao.jpg', null=True, upload_to='foto_card/%d/%m%Y')),
            ],
        ),
        migrations.DeleteModel(
            name='Ferramenta',
        ),
        migrations.AddField(
            model_name='profissional',
            name='foto_profissional',
            field=models.ImageField(default='core/static/imagem_padrao/padrao.jpg', upload_to='foto/%d/%m%Y'),
        ),
        migrations.AddField(
            model_name='profissional',
            name='identidade_profissional',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Carteira de Identidade Profissional'),
        ),
    ]
