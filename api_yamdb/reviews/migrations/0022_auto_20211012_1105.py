# Generated by Django 2.2.16 on 2021-10-12 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0021_remove_title_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={},
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.SmallIntegerField(choices=[(1, 'admin'), (2, 'moderator'), (3, 'user')], default=3),
        ),
    ]
