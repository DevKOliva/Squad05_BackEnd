# Generated by Django 5.1.2 on 2024-10-18 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_delete_textinho_categoria_classe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video',
        ),
        migrations.AddField(
            model_name='video',
            name='videos',
            field=models.ImageField(default='', upload_to='fotos/%d/%m/%Y'),
        ),
    ]