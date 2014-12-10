# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabshare', '0002_auto_20141207_1954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cab_sharing',
            options={'ordering': ['-travel_date', '-travel_time'], 'verbose_name': 'Cab Sharing'},
        ),
        migrations.RemoveField(
            model_name='cab_sharing',
            name='date_time',
        ),
        migrations.AddField(
            model_name='cab_sharing',
            name='travel_date',
            field=models.DateField(help_text=b'Date on which cab is required', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cab_sharing',
            name='travel_time',
            field=models.TimeField(help_text=b'Time when cab is required', null=True),
            preserve_default=True,
        ),
    ]
