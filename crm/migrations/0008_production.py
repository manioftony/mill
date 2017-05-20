# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_employeeinfo_total_working_hour_per_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.PositiveIntegerField(default=2, choices=[(0, b'Inactive'), (2, b'Active')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('kg', models.IntegerField(max_length=100, null=True, blank=True)),
                ('date', models.DateField(max_length=100, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
