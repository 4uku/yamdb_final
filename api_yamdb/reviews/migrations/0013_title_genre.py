# Generated by Django 2.2.16 on 2021-10-09 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0012_auto_20211009_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='genre_title', to='reviews.Genre'),
        ),
    ]
