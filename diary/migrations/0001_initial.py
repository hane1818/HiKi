# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('content', models.CharField(blank=True, max_length=1000)),
                ('weather_meantemp', models.CharField(max_length=50, null=True)),
                ('weather_cond', models.CharField(max_length=50, null=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50, null=True)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=13, null=True)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('img', models.FileField(upload_to='user_media/')),
                ('diary', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='diary.Diary')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagName', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='diary',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='diary.Map'),
        ),
        migrations.AddField(
            model_name='diary',
            name='tags',
            field=models.ManyToManyField(to='diary.Tag'),
        ),
    ]
