# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0020_auto_20170621_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='post_type',
            field=models.CharField(choices=[('Private', 'Private'), ('Public', 'Public')], default='Private', max_length=30),
        ),
    ]
