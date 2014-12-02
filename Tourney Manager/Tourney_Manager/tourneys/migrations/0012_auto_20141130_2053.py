# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tourneys', '0011_auto_20141129_0515'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='Owner',
            field=models.ForeignKey(related_name=b'owner', default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tourney',
            name='Winner',
            field=models.ForeignKey(related_name=b'winner', default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
