# Generated by Django 4.0.4 on 2022-07-04 12:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('medetsin_app', '0002_remove_jamoa_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='jamoa',
            name='malumoti',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jamoa',
            name='soat',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
