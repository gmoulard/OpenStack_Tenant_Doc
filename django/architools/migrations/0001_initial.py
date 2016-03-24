# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TenantList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('ID_T', models.CharField(max_length=200)),
                ('OS_REGION_NAME', models.CharField(max_length=200)),
                ('OS_TENANT_ID', models.CharField(max_length=200)),
                ('OS_TENANT_NAME', models.CharField(max_length=200)),
                ('OS_PROJECT_NAME', models.CharField(max_length=200)),
                ('OS_USERNAME', models.CharField(max_length=200)),
                ('OS_PASSWORD', models.CharField(max_length=200)),
            ],
        ),
    ]