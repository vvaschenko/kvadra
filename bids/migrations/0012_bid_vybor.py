# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-24 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0011_remove_bidimport_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='vybor',
            field=models.IntegerField(default=0),
        ),
    ]