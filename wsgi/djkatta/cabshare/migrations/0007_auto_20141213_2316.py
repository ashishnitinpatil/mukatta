# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabshare', '0006_auto_20141212_0102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cab_sharing',
            options={'ordering': ['travel_date', 'travel_time'], 'verbose_name': 'Cab Sharing'},
        ),
        migrations.AlterField(
            model_name='cab_sharing',
            name='pickup_from',
            field=models.CharField(help_text=b'Pickup location', max_length=128, blank=True),
        ),
    ]
