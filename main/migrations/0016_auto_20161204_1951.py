# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-04 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20161204_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passbook',
            name='s_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.User'),
        ),
        migrations.AlterField(
            model_name='passbook',
            name='work',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userlocation',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
    ]
