# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-16 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20161115_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='near_by',
            field=models.CharField(default='0.0', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
    ]
