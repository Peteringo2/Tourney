# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0019_remove_match_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='Round_number',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
