# Generated by Django 5.1.2 on 2024-10-18 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_textinho'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Textinho',
        ),
        migrations.AddField(
            model_name='categoria',
            name='classe',
            field=models.CharField(default='', max_length=50, verbose_name='qual a classe no css'),
        ),
    ]
