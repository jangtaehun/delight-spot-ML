# Generated by Django 5.0.5 on 2024-05-27 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='description',
        ),
    ]
