# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-05 07:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0006_auto_20170406_2007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storagemedium',
            old_name='number_of_mounts',
            new_name='num_of_mounts',
        ),
    ]
