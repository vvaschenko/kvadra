# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-11-11 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
