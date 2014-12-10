# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cab_sharing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('req_open', models.CharField(default=True, help_text=b'Status of the request', max_length=2, verbose_name=b'Request Status', choices=[(b'O', b'Open'), (b'C', b'Closed')])),
                ('contact_number', models.BigIntegerField(help_text=b'Contact number (optional)', null=True, blank=True)),
                ('date_time', models.DateTimeField(help_text=b'Date & time when cab is required')),
                ('destination', models.CharField(default=b'Airport', max_length=64)),
                ('already_booked', models.BooleanField(default=False, help_text=b'Already booked a cab?')),
                ('pickup_from', models.CharField(max_length=128, blank=True)),
                ('estimated_cost', models.BigIntegerField(help_text=b'Estimated total cost of the trip by cab', null=True, blank=True)),
                ('cab_company', models.CharField(help_text=b'Name of the cab company', max_length=64, blank=True)),
                ('cab_type', models.CharField(help_text=b'Type of the cab (mini, sedan, rickshaw)', max_length=32, blank=True)),
                ('passengers', models.IntegerField(default=0, help_text=b'Number of accompanying passengers')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'ordering': ['-date_time'],
                'verbose_name': 'Cab Sharing',
            },
            bases=(models.Model,),
        ),
    ]
