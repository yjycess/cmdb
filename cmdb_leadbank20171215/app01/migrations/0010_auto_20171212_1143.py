# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-12-12 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_auto_20171212_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operate_file',
            name='upload_file',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='operate_file',
            name='upload_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='operate_file',
            name='upload_path',
            field=models.CharField(max_length=64),
        ),
    ]
