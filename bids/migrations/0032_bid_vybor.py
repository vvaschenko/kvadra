# Generated by Django 2.1.5 on 2019-06-18 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0031_auto_20190618_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='vybor',
            field=models.BooleanField(default=False),
        ),
    ]
