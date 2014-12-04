# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0016_auto_20141202_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='Periodicity',
            field=models.IntegerField(default=30),
            preserve_default=True,
        ),
    ]
