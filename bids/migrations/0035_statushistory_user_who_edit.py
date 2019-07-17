# Generated by Django 2.1.5 on 2019-06-24 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bids', '0034_auto_20190624_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='statushistory',
            name='user_who_edit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь изменивший этот статус'),
        ),
    ]
