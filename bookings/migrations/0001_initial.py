# Generated by Django 5.0.6 on 2024-05-15 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('kind', models.CharField(choices=[('food_store', '음식점'), ('cafe', '카페')], max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]