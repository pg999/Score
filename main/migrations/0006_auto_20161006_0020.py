# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-05 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160926_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
        migrations.AlterField(
            model_name='post_response',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Post'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
