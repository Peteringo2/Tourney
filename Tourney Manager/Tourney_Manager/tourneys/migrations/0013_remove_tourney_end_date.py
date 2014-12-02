# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0012_auto_20141130_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourney',
            name='End_date',
        ),
    ]
