# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cabshare', '0004_auto_20141211_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cab_sharing',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='cab_sharing',
            name='passengers',
            field=models.IntegerField(help_text=b'Number of accompanying passengers', null=True, blank=True),
        ),
    ]
