# Generated by Django 2.2 on 2019-08-21 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0005_auto_20190811_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='commentary',
            field=models.TextField(blank=True, max_length=999),
        ),
    ]
