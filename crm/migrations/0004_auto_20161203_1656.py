# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20161130_0605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.PositiveIntegerField(default=2, choices=[(0, b'Inactive'), (2, b'Active')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100, null=True, blank=True)),
                ('last_name', models.CharField(max_length=100, null=True, blank=True)),
                ('gender', models.PositiveIntegerField(blank=True, null=True, choices=[(0, b'Male'), (2, b'Female')])),
                ('blood_group', models.CharField(max_length=100, null=True, blank=True)),
                ('current_address', models.CharField(max_length=100, null=True, blank=True)),
                ('permanet_address', models.CharField(max_length=100, null=True, blank=True)),
                ('joining_date', models.DateField(max_length=100, null=True, blank=True)),
                ('date_of_birth', models.DateField(max_length=100, null=True, blank=True)),
                ('mobile_number', models.IntegerField(null=True, blank=True)),
                ('landline_number', models.IntegerField(null=True, blank=True)),
                ('voter_id', models.CharField(max_length=100, null=True, blank=True)),
                ('driving_license', models.CharField(max_length=100, null=True, blank=True)),
                ('aadhar_card', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='resume',
            field=models.FileField(null=True, upload_to=b'static/resume/img/%Y/%m/%d', blank=True),
        ),
    ]
