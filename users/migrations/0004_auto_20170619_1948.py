# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170526_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default='', help_text='Describe yourself with 500 characters or less. There will be no formatting.', max_length=1000, verbose_name='biography'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to=users.models.photo_upload_to, verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='User name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='verified',
            field=models.BooleanField(default=False, help_text='Designates whether the user has verified email ownership.', verbose_name='verified'),
        ),
    ]
