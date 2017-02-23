"""
    ESSArch is an open source archiving and digital preservation system

    ESSArch Core
    Copyright (C) 2005-2017 ES Solutions AB

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

    Contact information:
    Web - http://www.essolutions.se
    Email - essarch@essolutions.se
"""

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-17 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkflowEngine', '0030_auto_20160817_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='archiveobject',
            name='checksum',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='archiveobject',
            name='checksum_algorithm',
            field=models.CharField(choices=[('md5', 'MD5'), ('sha1', 'SHA-1'), ('sha224', 'SHA-224'), ('sha256', 'SHA-256'), ('sha384', 'SHA-384'), ('sha512', 'SHA-512')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='archiveobject',
            name='filesize',
            field=models.IntegerField(null=True),
        ),
    ]