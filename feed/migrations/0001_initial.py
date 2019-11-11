# Generated by Django 2.2 on 2019-06-05 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('image', models.FilePathField(path='/img')),
                ('caption', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('link', models.CharField(max_length=100)),
            ],
        ),
    ]
