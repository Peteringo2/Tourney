# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0008_remove_user_profile_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='Nickname',
            field=models.CharField(default=b'Default', max_length=50),
            preserve_default=True,
        ),
    ]
