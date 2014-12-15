# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabshare', '0008_cab_sharing_travel_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cab_sharing',
            name='travel_datetime',
            field=models.DateTimeField(help_text=b'Internal field', null=True, blank=True),
        ),
    ]
