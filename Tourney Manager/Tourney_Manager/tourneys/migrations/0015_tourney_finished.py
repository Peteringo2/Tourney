# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0014_remove_tourney_started'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='Finished',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
