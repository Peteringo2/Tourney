# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0024_auto_20141204_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='Match_Pointer',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='Match_number',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
