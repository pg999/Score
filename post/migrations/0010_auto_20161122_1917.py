# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-22 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20161122_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='work',
            new_name='post_work',
        ),
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
    ]
