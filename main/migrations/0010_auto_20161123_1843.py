# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-23 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_userlocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlocation',
            name='user_id',
            field=models.CharField(default='1', max_length=5),
        ),
    ]
