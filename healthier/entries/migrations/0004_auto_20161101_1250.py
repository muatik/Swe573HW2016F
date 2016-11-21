# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import entries.models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_auto_20161031_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='extra',
            field=entries.models.JSONField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='entry',
            name='what',
            field=models.CharField(max_length=200),
        ),
    ]
