# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-22 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_post_post_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='payment',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
    ]