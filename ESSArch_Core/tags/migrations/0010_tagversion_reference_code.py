# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-13 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0009_auto_20180530_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagversion',
            name='reference_code',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterModelOptions(
            name='tagversion',
            options={'get_latest_by': 'create_date', 'ordering': ('reference_code',)},
        ),
    ]
