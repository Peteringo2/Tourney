# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0017_tourney_periodicity'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='Check_in',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
