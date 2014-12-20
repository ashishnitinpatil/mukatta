# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomreq', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room_requirement',
            options={'ordering': ['-modified_on'], 'verbose_name': 'Room Requirement'},
        ),
        migrations.RemoveField(
            model_name='room_requirement',
            name='valid_hash',
        ),
        migrations.RemoveField(
            model_name='room_requirement',
            name='valid_upto',
        ),
        migrations.AddField(
            model_name='room_requirement',
            name='available_from',
            field=models.DateField(help_text=b'When would the room be available for accomodation?', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room_requirement',
            name='contact_number',
            field=models.CharField(help_text=b'Contact number (optional)', max_length=16, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room_requirement',
            name='deposit',
            field=models.IntegerField(help_text=b'Security deposit (in Rs.)', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room_requirement',
            name='gender_req',
            field=models.CharField(default=b'A', help_text=b'Gender requirement', max_length=2, verbose_name=b'Gender requirement', choices=[(b'M', b'Male'), (b'F', b'Female'), (b'A', b'Any')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room_requirement',
            name='immediate_possession',
            field=models.BooleanField(default=True, help_text=b'Is the room available for immediate possession?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room_requirement',
            name='locality',
            field=models.CharField(help_text=b'Name of locality/society', max_length=64, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room_requirement',
            name='modified_on',
            field=models.DateTimeField(help_text=b'Internal field', auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room_requirement',
            name='more_details',
            field=models.CharField(help_text=b'Additional details', max_length=2048, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room_requirement',
            name='rent',
            field=models.IntegerField(help_text=b'Rent per month (in Rs.)', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room_requirement',
            name='req_open',
            field=models.CharField(default=b'O', help_text=b'Status of the request', max_length=2, verbose_name=b'Request Status', choices=[(b'O', b'Open'), (b'C', b'Closed')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='room_requirement',
            name='vacancies',
            field=models.IntegerField(default=1, help_text=b'Total vacancies (no. of persons)'),
            preserve_default=True,
        ),
    ]
