# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-24 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0008_auto_20170223_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivepolicy',
            name='receive_extract_sip',
            field=models.BooleanField(default=False, verbose_name=b'Extract SIP on receive'),
        ),
    ]
