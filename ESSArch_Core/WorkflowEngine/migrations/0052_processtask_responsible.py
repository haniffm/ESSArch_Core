# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 08:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WorkflowEngine', '0051_processtask_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='processtask',
            name='responsible',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
