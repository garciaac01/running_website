# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-22 01:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('running_site', '0005_auto_20171221_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='seconds',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, validators=[django.core.validators.MaxValueValidator(60.0), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
