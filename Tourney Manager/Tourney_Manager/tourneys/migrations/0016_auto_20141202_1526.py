# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0015_tourney_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='Id_round',
            field=models.ForeignKey(to='tourneys.Round'),
        ),
        migrations.AlterField(
            model_name='round',
            name='Id_tourney',
            field=models.ForeignKey(to='tourneys.Tourney'),
        ),
        migrations.AlterField(
            model_name='user_match',
            name='Id_match',
            field=models.ForeignKey(to='tourneys.Match'),
        ),
        migrations.AlterField(
            model_name='user_match',
            name='Id_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user_tourney',
            name='Id_tourney',
            field=models.ForeignKey(to='tourneys.Tourney'),
        ),
        migrations.AlterField(
            model_name='user_tourney',
            name='Id_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
