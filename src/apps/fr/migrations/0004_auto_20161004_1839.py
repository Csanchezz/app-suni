# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 18:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fr', '0003_auto_20161004_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='etiqueta',
            name='color',
            field=models.CharField(choices=[('info', 'celestito'), ('danger', 'rojo'), ('success', 'verde')], default='info', max_length=10),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2016, 10, 4, 18, 39, 42, 976495, tzinfo=utc)),
        ),
    ]
