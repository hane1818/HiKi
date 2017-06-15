# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 04:12
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tally',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('type', models.CharField(max_length=20)),
                ('subtype', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=0, default=Decimal('0'), max_digits=10)),
                ('notes', models.CharField(max_length=200)),
            ],
        ),
    ]
