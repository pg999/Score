# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-08 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20161007_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='post_response',
            name='post_id',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
