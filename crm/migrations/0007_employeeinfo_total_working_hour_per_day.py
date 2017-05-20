# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20161203_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeinfo',
            name='total_working_hour_per_day',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
