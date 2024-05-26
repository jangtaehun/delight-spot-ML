# Generated by Django 5.0.5 on 2024-05-23 13:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_initial'),
        ('userGroup', '0004_remove_group_sharedlist'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='my_groups', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sharedlist',
            name='store',
            field=models.ManyToManyField(default=1, related_name='share_list', to='stores.store'),
        ),
    ]
