# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturier', '0002_auto_20170622_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='Proposal_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
