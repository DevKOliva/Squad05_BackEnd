# Generated by Django 5.1.2 on 2024-10-18 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_remove_video_video_video_videos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='videos',
        ),
        migrations.AddField(
            model_name='video',
            name='imgvideo',
            field=models.ImageField(default='', upload_to='fotos/%d/%m/%Y'),
        ),
    ]
