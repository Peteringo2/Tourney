# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0018_tourney_check_in'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='Start_date',
        ),
    ]
