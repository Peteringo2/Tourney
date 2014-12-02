# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0009_code_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='Id_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
