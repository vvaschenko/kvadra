# Generated by Django 2.1.5 on 2019-06-14 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0029_auto_20190614_0837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statushistory',
            old_name='created_dt',
            new_name='created_date',
        ),
    ]