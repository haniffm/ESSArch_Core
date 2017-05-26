# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-23 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0007_auto_20170223_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivepolicy',
            name='cache_extracted_age',
            field=models.IntegerField(null=True, verbose_name=b'Maximum age (days) of extracted package before deletion from cache'),
        ),
        migrations.AddField(
            model_name='archivepolicy',
            name='cache_extracted_size',
            field=models.BigIntegerField(null=True, verbose_name=b'Maximum size (bytes) of extracted package before deletion from cache'),
        ),
        migrations.AddField(
            model_name='archivepolicy',
            name='cache_package_age',
            field=models.IntegerField(null=True, verbose_name=b'Maximum age (days) of package before deletion from cache'),
        ),
        migrations.AddField(
            model_name='archivepolicy',
            name='cache_package_size',
            field=models.BigIntegerField(null=True, verbose_name=b'Maximum size (bytes) of package before deletion from cache'),
        ),
        migrations.AddField(
            model_name='archivepolicy',
            name='index',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='archivepolicy',
            name='wait_for_approval',
            field=models.BooleanField(default=True, verbose_name=b'Wait for approval'),
        ),
    ]
