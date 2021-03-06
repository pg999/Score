# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-23 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_auto_20161123_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_work',
            new_name='work',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
    ]
