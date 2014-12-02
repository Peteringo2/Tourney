# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0013_remove_tourney_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourney',
            name='Started',
        ),
    ]
