# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabshare', '0003_auto_20141209_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cab_sharing',
            name='estimated_cost',
            field=models.IntegerField(help_text=b'Estimated total cost of the trip by cab', null=True, blank=True),
        ),
    ]
