# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-09 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0007_auto_20170609_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
