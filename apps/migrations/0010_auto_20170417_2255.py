# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_auto_20170225_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(max_length=9192),
        ),
    ]
