# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-12-12 03:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_operate_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='operate_file',
            name='upload_name',
            field=models.CharField(default=datetime.datetime(2017, 12, 12, 3, 29, 35, 575000, tzinfo=utc), max_length=64, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='operate_file',
            name='upload_host',
            field=models.CharField(max_length=255),
        ),
    ]
