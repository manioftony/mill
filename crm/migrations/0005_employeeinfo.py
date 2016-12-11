# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20161203_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.PositiveIntegerField(default=2, choices=[(0, b'Inactive'), (2, b'Active')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('employee_id', models.CharField(max_length=100, null=True, blank=True)),
                ('working_shift', models.CharField(max_length=100, null=True, blank=True)),
                ('login_time', models.DateTimeField(null=True, blank=True)),
                ('logout_time', models.DateTimeField(null=True, blank=True)),
                ('employee_role', models.CharField(max_length=100, null=True, blank=True)),
                ('under_supervision', models.CharField(max_length=100, null=True, blank=True)),
                ('break_time', models.DateTimeField(null=True, blank=True)),
                ('over_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
