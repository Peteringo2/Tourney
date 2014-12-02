# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0010_auto_20141124_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='Creation_date',
            field=models.DateTimeField(default=datetime.date(2014, 11, 29), verbose_name=b'Creation Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tourney',
            name='Max_participants',
            field=models.IntegerField(default=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tourney',
            name='Started',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
