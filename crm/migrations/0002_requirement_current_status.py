# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='current_status',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'open'), (1, b'in progress'), (2, b'closed')]),
            preserve_default=True,
        ),
    ]
