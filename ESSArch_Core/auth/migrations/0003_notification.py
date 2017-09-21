# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-14 13:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ess.auth', '0002_auto_20170622_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(choices=[(10, b'debug'), (20, b'info'), (30, b'warning'), (40, b'error'), (50, b'critical')])),
                ('message', models.CharField(max_length=255)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created'],
                'get_latest_by': 'time_created',
            },
        ),
    ]