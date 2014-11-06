# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0007_auto_20141103_0320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='Nickname',
        ),
    ]
