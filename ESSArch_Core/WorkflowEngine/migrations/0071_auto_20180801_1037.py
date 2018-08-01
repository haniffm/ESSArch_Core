# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-01 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkflowEngine', '0070_auto_20180801_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='processstep',
            name='on_error',
            field=models.ManyToManyField(related_name='steps_on_errors', to='WorkflowEngine.ProcessTask'),
        ),
        migrations.AddField(
            model_name='processtask',
            name='on_error',
            field=models.ManyToManyField(related_name='_processtask_on_error_+', to='WorkflowEngine.ProcessTask'),
        ),
    ]
