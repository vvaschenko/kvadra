# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-06 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0003_auto_20190426_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='family_income',
            field=models.IntegerField(verbose_name=b'\xd0\xa1\xd1\x96\xd0\xbc\xd0\xb5\xd0\xb9\xd0\xbd\xd0\xb8\xd0\xb9 \xd0\x94\xd0\xbe\xd1\x85\xd1\x96\xd0\xb4'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='income',
            field=models.IntegerField(verbose_name=b'\xd0\x94\xd0\xbe\xd1\x85\xd1\x96\xd0\xb4'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='other_income',
            field=models.IntegerField(verbose_name=b'\xd0\x86\xd0\xbd\xd1\x88\xd0\xb8\xd0\xb9 \xd0\x94\xd0\xbe\xd1\x85\xd1\x96\xd0\xb4'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='total_income',
            field=models.IntegerField(verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb8\xd0\xb9 \xd0\x94\xd0\xbe\xd1\x85\xd1\x96\xd0\xb4'),
        ),
    ]
