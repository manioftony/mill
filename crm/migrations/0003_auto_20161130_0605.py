# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_requirement_current_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='resume',
            field=models.FileField(null=True, upload_to=b'resume/img/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requirement',
            name='current_status',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'open'), (1, b'In progress'), (2, b'closed')]),
        ),
    ]
