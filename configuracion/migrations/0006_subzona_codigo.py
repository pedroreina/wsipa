# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0005_auto_20160722_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='subzona',
            name='codigo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]