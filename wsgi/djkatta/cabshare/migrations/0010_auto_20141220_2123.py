# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabshare', '0009_auto_20141215_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cab_sharing',
            name='req_open',
            field=models.CharField(default=b'O', help_text=b'Status of the request', max_length=2, verbose_name=b'Request Status', choices=[(b'O', b'Open'), (b'C', b'Closed')]),
        ),
    ]
