# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-15 15:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_schedule', '0011_auto_20160515_1327'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ViewerType',
        ),
        migrations.AddField(
            model_name='ticket',
            name='date',
            field=models.DateField(default=datetime.date(2016, 5, 15)),
        ),
    ]
