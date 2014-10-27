# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourneys', '0002_auto_20141013_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tourney',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=50)),
                ('Game', models.CharField(max_length=50)),
                ('Start_date', models.DateTimeField(verbose_name=b'Start Date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Tourneys',
        ),
    ]
