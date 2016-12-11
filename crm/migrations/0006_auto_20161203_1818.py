# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_employeeinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeinfo',
            name='break_time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='login_time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='logout_time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='over_time',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
