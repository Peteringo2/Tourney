# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0025_auto_20141204_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='Created_rounds',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
