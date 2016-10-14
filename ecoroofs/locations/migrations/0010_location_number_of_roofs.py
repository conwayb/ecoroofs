# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0009_add_contractor_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='number_of_roofs',
            field=models.PositiveIntegerField(default=1, verbose_name='Number of unique roofs at this location'),
        ),
    ]
