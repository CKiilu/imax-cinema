# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-31 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie_schedule', '0018_auto_20160516_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
