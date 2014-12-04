# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0021_remove_round_round_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='Round_number',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
