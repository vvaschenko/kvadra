# Generated by Django 2.1.5 on 2019-06-19 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190612_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='mailing_list',
            field=models.BooleanField(default=True, verbose_name='Участь в розсилках'),
        ),
    ]