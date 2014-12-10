# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabshare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cab_sharing',
            name='contact_number',
            field=models.CharField(help_text=b'Contact number (optional)', max_length=16, blank=True),
        ),
    ]
