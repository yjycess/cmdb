# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-12-06 03:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_device_machine_room_cabinet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Machine_Room',
            new_name='Operate_Room',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='machine_room',
            new_name='operate_room',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='machine_room_Cabinet',
            new_name='operate_room_Cabinet',
        ),
    ]
