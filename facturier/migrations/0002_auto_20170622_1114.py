# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 09:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturier', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Statuses'},
        ),
    ]
