# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.PositiveIntegerField(default=2, choices=[(0, b'Inactive'), (2, b'Active')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('location', models.CharField(max_length=100, null=True, blank=True)),
                ('type_of_company', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrgInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.PositiveIntegerField(default=2, choices=[(0, b'Inactive'), (2, b'Active')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('customer_name', models.CharField(max_length=200, null=True, blank=True)),
                ('customer_created', models.DateField(null=True, blank=True)),
                ('no_of_profile', models.IntegerField(null=True, blank=True)),
                ('no_of_donation', models.IntegerField(null=True, blank=True)),
                ('total_amount', models.IntegerField(null=True, blank=True)),
                ('sub_domain', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.PositiveIntegerField(default=2, choices=[(0, b'Inactive'), (2, b'Active')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('position', models.CharField(max_length=100, null=True, blank=True)),
                ('no_openings', models.CharField(max_length=100, null=True, blank=True)),
                ('technology', models.CharField(max_length=100, null=True, blank=True)),
                ('skills', models.CharField(max_length=100, null=True, blank=True)),
                ('experience', models.CharField(max_length=100, null=True, blank=True)),
                ('location', models.CharField(max_length=100, null=True, blank=True)),
                ('type_of_opening', models.CharField(max_length=100, null=True, blank=True)),
                ('salary_range', models.CharField(max_length=100, null=True, blank=True)),
                ('unique_id', models.CharField(max_length=100, unique=True, null=True)),
                ('company', models.ForeignKey(blank=True, to='crm.Company', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
