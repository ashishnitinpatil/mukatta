# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pass_reset_validb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=32)),
                ('valid_hash', models.CharField(max_length=16)),
                ('valid_upto', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
