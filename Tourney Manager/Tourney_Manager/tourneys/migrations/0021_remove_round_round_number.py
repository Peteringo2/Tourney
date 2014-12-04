# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0020_round_round_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='round',
            name='Round_number',
        ),
    ]
