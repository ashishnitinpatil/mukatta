# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20141114_0126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pass_reset_validb',
            options={'ordering': ['-valid_upto'], 'verbose_name': 'Password Reset Hashtable'},
        ),
    ]
