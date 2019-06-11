# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-08 10:06
from __future__ import unicode_literals

import users.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0008_auto_20190506_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='biddouble',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bids.BidStatus', verbose_name='Статус заявки'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='House_number_fiz',
            field=models.CharField(blank=True, max_length=10, verbose_name='Номер Будинку Проживання'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='House_number_ur',
            field=models.CharField(blank=True, max_length=10, verbose_name='Номер Будинку Реєстрації'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='apartment_number_fiz',
            field=models.CharField(blank=True, max_length=10, verbose_name='Номер Квартири Проживання'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='apartment_number_ur',
            field=models.CharField(blank=True, max_length=10, verbose_name='Номер Квартири Реєстрації'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='base_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='ID бази'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='birthday',
            field=models.CharField(blank=True, max_length=10, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='city',
            field=models.CharField(max_length=128, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='cod_number_phone1',
            field=models.CharField(blank=True, max_length=4, verbose_name='Код телефона 1'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='cod_number_phone2',
            field=models.CharField(blank=True, max_length=4, verbose_name='Код телефона 2'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='cod_number_phone3',
            field=models.CharField(blank=True, max_length=4, verbose_name='Код телефона 3'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='cod_number_phone4',
            field=models.CharField(blank=True, max_length=4, verbose_name='Код телефона 4'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='cod_number_phone5',
            field=models.CharField(blank=True, max_length=4, verbose_name='Код телефона 5'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='cod_number_phone_work',
            field=models.CharField(blank=True, max_length=10, verbose_name='Код телефона рабочий'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='contact_phone',
            field=models.CharField(max_length=12, validators=[users.validators.validate_contact_phone_numeric, users.validators.validate_contact_phone_length], verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='credit_sum',
            field=models.IntegerField(blank=True, null=True, verbose_name='Сумма кредита'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='date_of_issue',
            field=models.DateField(null=True, verbose_name='Паспорт Дата Видачі'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='family_income',
            field=models.IntegerField(blank=True, verbose_name='Сімейний Дохід'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='groupid',
            field=models.IntegerField(blank=True, null=True, verbose_name='ID группы'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='income',
            field=models.IntegerField(blank=True, verbose_name='Дохід'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='issued_by',
            field=models.CharField(blank=True, max_length=255, verbose_name='Паспорт Ким Видано'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='itn',
            field=models.CharField(blank=True, max_length=10, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='lead_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='ID клиента'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='mailing_list',
            field=models.CharField(blank=True, max_length=255, verbose_name='Участь в розсилках'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='name_base',
            field=models.CharField(blank=True, max_length=255, verbose_name='Назва Бази'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='name_project',
            field=models.CharField(blank=True, max_length=255, verbose_name='Назва проекту'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='number_Telegram',
            field=models.CharField(blank=True, max_length=30, verbose_name='Номер Telegram'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='number_Viber',
            field=models.CharField(blank=True, max_length=30, verbose_name='Номер Viber'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='number_WhatsApp',
            field=models.CharField(blank=True, max_length=30, verbose_name='Номер WhatsApp'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='number_phone1',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона 1'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='number_phone2',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона 2'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='number_phone3',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона 3'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='number_phone4',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона 4'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='number_phone5',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона 5'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='number_phone_work',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона рабочий'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='other_income',
            field=models.IntegerField(blank=True, verbose_name='Інший Дохід'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='partner_name',
            field=models.CharField(choices=[('easysoft', 'EasySoft(EasyPay)'), ('admitad', 'Admitad'), ('salesdoubler', 'Salesdoubler'), ('website', 'Website'), ('doaffiliate', 'Doaffiliate'), ('linkprofit', 'Linkprofit'), ('hotline', 'HotLine'), ('treeum', 'Treeum'), ('turnes', 'Turnes'), ('recommendation', 'Рекомендация'), ('lifecell', 'Lifecell'), ('city24', 'City24')], max_length=32, verbose_name='Партнер'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='passport_number',
            field=models.CharField(blank=True, max_length=32, verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='passport_series',
            field=models.CharField(blank=True, max_length=16, validators=[users.validators.validate_passport_series], verbose_name='Серия паспорта'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='place_of_work',
            field=models.CharField(blank=True, max_length=255, verbose_name='Місце Роботи'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='position',
            field=models.CharField(blank=True, max_length=255, verbose_name='Посада'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='project_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='ID проекту'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='registration_area_fiz',
            field=models.CharField(blank=True, max_length=255, verbose_name='Область Проживання'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='registration_area_ur',
            field=models.CharField(blank=True, max_length=255, verbose_name='Область Реєстрації'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='registration_city_fiz',
            field=models.CharField(blank=True, max_length=255, verbose_name='Місто Проживання'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='registration_city_ur',
            field=models.CharField(blank=True, max_length=255, verbose_name='Місто Реєстрації'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='registration_raion_fiz',
            field=models.CharField(blank=True, max_length=255, verbose_name='Район Проживання'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='registration_raion_ur',
            field=models.CharField(blank=True, max_length=255, verbose_name='Район Реєстрації'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='registration_street_fiz',
            field=models.CharField(blank=True, max_length=255, verbose_name='Вулиця Проживання'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='registration_street_ur',
            field=models.CharField(blank=True, max_length=255, verbose_name='Вулиця Реєстрації'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='remark',
            field=models.CharField(blank=True, max_length=255, verbose_name='Примітка'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bids.BidStatus', verbose_name='Статус заявки'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='status_Viber',
            field=models.CharField(blank=True, max_length=255, verbose_name='Статус Viber'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='total_income',
            field=models.IntegerField(blank=True, verbose_name='Загальний Дохід'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='updated_dt',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_bids', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь изменивший эту заявку'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='webmaster_id',
            field=models.CharField(blank=True, max_length=32, verbose_name='Webmaster ID'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='House_number_fiz',
            field=models.CharField(blank=True, max_length=10, verbose_name='Номер Будинку Проживання'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='House_number_ur',
            field=models.CharField(blank=True, max_length=10, verbose_name='Номер Будинку Реєстрації'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='apartment_number_fiz',
            field=models.CharField(blank=True, max_length=10, verbose_name='Номер Квартири Проживання'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='apartment_number_ur',
            field=models.CharField(blank=True, max_length=10, verbose_name='Номер Квартири Реєстрації'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='base_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='ID бази'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='birthday',
            field=models.CharField(blank=True, max_length=10, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='city',
            field=models.CharField(max_length=128, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='cod_number_phone1',
            field=models.CharField(blank=True, max_length=4, verbose_name='Код телефона 1'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='cod_number_phone2',
            field=models.CharField(blank=True, max_length=4, verbose_name='Код телефона 2'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='cod_number_phone3',
            field=models.CharField(blank=True, max_length=4, verbose_name='Код телефона 3'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='cod_number_phone4',
            field=models.CharField(blank=True, max_length=4, verbose_name='Код телефона 4'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='cod_number_phone5',
            field=models.CharField(blank=True, max_length=4, verbose_name='Код телефона 5'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='cod_number_phone_work',
            field=models.CharField(blank=True, max_length=10, verbose_name='Код телефона рабочий'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='contact_phone',
            field=models.CharField(max_length=12, validators=[users.validators.validate_contact_phone_numeric, users.validators.validate_contact_phone_length], verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='credit_sum',
            field=models.IntegerField(blank=True, null=True, verbose_name='Сумма кредита'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='date_of_issue',
            field=models.DateField(null=True, verbose_name='Паспорт Дата Видачі'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='family_income',
            field=models.IntegerField(default=0, null=True, verbose_name='Сімейний Дохід'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='groupid',
            field=models.IntegerField(blank=True, null=True, verbose_name='ID группы'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='income',
            field=models.IntegerField(default=0, null=True, verbose_name='Дохід'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='issued_by',
            field=models.CharField(blank=True, max_length=255, verbose_name='Паспорт Ким Видано'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='itn',
            field=models.CharField(blank=True, max_length=10, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='lead_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='ID клиента'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='mailing_list',
            field=models.CharField(blank=True, max_length=255, verbose_name='Участь в розсилках'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='name_base',
            field=models.CharField(blank=True, max_length=255, verbose_name='Назва Бази'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='name_project',
            field=models.CharField(blank=True, max_length=255, verbose_name='Назва проекту'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='number_Telegram',
            field=models.CharField(blank=True, max_length=30, verbose_name='Номер Telegram'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='number_Viber',
            field=models.CharField(blank=True, max_length=30, verbose_name='Номер Viber'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='number_WhatsApp',
            field=models.CharField(blank=True, max_length=30, verbose_name='Номер WhatsApp'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='number_phone1',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона 1'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='number_phone2',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона 2'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='number_phone3',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона 3'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='number_phone4',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона 4'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='number_phone5',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона 5'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='number_phone_work',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона рабочий'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='other_income',
            field=models.IntegerField(default=0, null=True, verbose_name='Інший Дохід'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='partner_name',
            field=models.CharField(choices=[('easysoft', 'EasySoft(EasyPay)'), ('admitad', 'Admitad'), ('salesdoubler', 'Salesdoubler'), ('website', 'Website'), ('doaffiliate', 'Doaffiliate'), ('linkprofit', 'Linkprofit'), ('hotline', 'HotLine'), ('treeum', 'Treeum'), ('turnes', 'Turnes'), ('recommendation', 'Рекомендация'), ('lifecell', 'Lifecell'), ('city24', 'City24')], max_length=32, verbose_name='Партнер'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='passport_number',
            field=models.CharField(blank=True, max_length=32, verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='passport_series',
            field=models.CharField(blank=True, max_length=16, validators=[users.validators.validate_passport_series], verbose_name='Серия паспорта'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='place_of_work',
            field=models.CharField(blank=True, max_length=255, verbose_name='Місце Роботи'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='position',
            field=models.CharField(blank=True, max_length=255, verbose_name='Посада'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='project_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='ID проекту'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='registration_area_fiz',
            field=models.CharField(blank=True, max_length=255, verbose_name='Область Проживання'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='registration_area_ur',
            field=models.CharField(blank=True, max_length=255, verbose_name='Область Реєстрації'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='registration_city_fiz',
            field=models.CharField(blank=True, max_length=255, verbose_name='Місто Проживання'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='registration_city_ur',
            field=models.CharField(blank=True, max_length=255, verbose_name='Місто Реєстрації'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='registration_raion_fiz',
            field=models.CharField(blank=True, max_length=255, verbose_name='Район Проживання'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='registration_raion_ur',
            field=models.CharField(blank=True, max_length=255, verbose_name='Район Реєстрації'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='registration_street_fiz',
            field=models.CharField(blank=True, max_length=255, verbose_name='Вулиця Проживання'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='registration_street_ur',
            field=models.CharField(blank=True, max_length=255, verbose_name='Вулиця Реєстрації'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='remark',
            field=models.CharField(blank=True, max_length=255, verbose_name='Примітка'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='status_Viber',
            field=models.CharField(blank=True, max_length=255, verbose_name='Статус Viber'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='total_income',
            field=models.IntegerField(default=0, null=True, verbose_name='Загальний Дохід'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='updated_dt',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь изменивший эту заявку'),
        ),
        migrations.AlterField(
            model_name='biddouble',
            name='webmaster_id',
            field=models.CharField(blank=True, max_length=32, verbose_name='Webmaster ID'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='House_number_fiz',
            field=models.CharField(blank=True, max_length=10, verbose_name='Номер Будинку Проживання'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='House_number_ur',
            field=models.CharField(blank=True, max_length=10, verbose_name='Номер Будинку Реєстрації'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='apartment_number_fiz',
            field=models.CharField(blank=True, max_length=10, verbose_name='Номер Квартири Проживання'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='apartment_number_ur',
            field=models.CharField(blank=True, max_length=10, verbose_name='Номер Квартири Реєстрації'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='base_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='ID бази'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='birthday',
            field=models.CharField(blank=True, max_length=10, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='city',
            field=models.CharField(max_length=128, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='cod_number_phone1',
            field=models.CharField(blank=True, max_length=4, verbose_name='Код телефона 1'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='cod_number_phone2',
            field=models.CharField(blank=True, max_length=4, verbose_name='Код телефона 2'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='cod_number_phone3',
            field=models.CharField(blank=True, max_length=4, verbose_name='Код телефона 3'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='cod_number_phone4',
            field=models.CharField(blank=True, max_length=4, verbose_name='Код телефона 4'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='cod_number_phone5',
            field=models.CharField(blank=True, max_length=4, verbose_name='Код телефона 5'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='cod_number_phone_work',
            field=models.CharField(blank=True, max_length=10, verbose_name='Код телефона рабочий'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='contact_phone',
            field=models.CharField(max_length=12, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='credit_sum',
            field=models.IntegerField(blank=True, null=True, verbose_name='Сумма кредита'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='date_of_issue',
            field=models.DateField(null=True, verbose_name='Паспорт Дата Видачі'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='family_income',
            field=models.IntegerField(default=0, null=True, verbose_name='Сімейний Дохід'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='groupid',
            field=models.IntegerField(blank=True, null=True, verbose_name='ID группы'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='income',
            field=models.IntegerField(default=0, null=True, verbose_name='Дохід'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='issued_by',
            field=models.CharField(blank=True, max_length=255, verbose_name='Паспорт Ким Видано'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='itn',
            field=models.CharField(blank=True, max_length=10, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='lead_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='ID клиента'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='mailing_list',
            field=models.CharField(blank=True, max_length=255, verbose_name='Участь в розсилках'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='name_base',
            field=models.CharField(blank=True, max_length=255, verbose_name='Назва Бази'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='name_project',
            field=models.CharField(blank=True, max_length=255, verbose_name='Назва проекту'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='number_Telegram',
            field=models.CharField(blank=True, max_length=30, verbose_name='Номер Telegram'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='number_Viber',
            field=models.CharField(blank=True, max_length=30, verbose_name='Номер Viber'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='number_WhatsApp',
            field=models.CharField(blank=True, max_length=30, verbose_name='Номер WhatsApp'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='number_phone1',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона 1'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='number_phone2',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона 2'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='number_phone3',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона 3'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='number_phone4',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона 4'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='number_phone5',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона 5'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='number_phone_work',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона рабочий'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='other_income',
            field=models.IntegerField(default=0, null=True, verbose_name='Інший Дохід'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='partner_name',
            field=models.CharField(max_length=32, verbose_name='Партнер'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='passport_number',
            field=models.CharField(blank=True, max_length=32, verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='passport_series',
            field=models.CharField(blank=True, max_length=16, verbose_name='Серия паспорта'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='place_of_work',
            field=models.CharField(blank=True, max_length=255, verbose_name='Місце Роботи'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='position',
            field=models.CharField(blank=True, max_length=255, verbose_name='Посада'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='project_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='ID проекту'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='registration_area_fiz',
            field=models.CharField(blank=True, max_length=255, verbose_name='Область Проживання'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='registration_area_ur',
            field=models.CharField(blank=True, max_length=255, verbose_name='Область Реєстрації'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='registration_city_fiz',
            field=models.CharField(blank=True, max_length=255, verbose_name='Місто Проживання'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='registration_city_ur',
            field=models.CharField(blank=True, max_length=255, verbose_name='Місто Реєстрації'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='registration_raion_fiz',
            field=models.CharField(blank=True, max_length=255, verbose_name='Район Проживання'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='registration_raion_ur',
            field=models.CharField(blank=True, max_length=255, verbose_name='Район Реєстрації'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='registration_street_fiz',
            field=models.CharField(blank=True, max_length=255, verbose_name='Вулиця Проживання'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='registration_street_ur',
            field=models.CharField(blank=True, max_length=255, verbose_name='Вулиця Реєстрації'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='remark',
            field=models.CharField(blank=True, max_length=255, verbose_name='Примітка'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='status_Viber',
            field=models.CharField(blank=True, max_length=255, verbose_name='Статус Viber'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='total_income',
            field=models.IntegerField(default=0, null=True, verbose_name='Загальний Дохід'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='updated_dt',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='bidimport',
            name='webmaster_id',
            field=models.CharField(blank=True, max_length=32, verbose_name='Webmaster ID'),
        ),
        migrations.AlterField(
            model_name='bidstatus',
            name='code',
            field=models.CharField(max_length=128, unique=True, verbose_name='Код статуса'),
        ),
        migrations.AlterField(
            model_name='bidstatus',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Имя/Название статуса'),
        ),
    ]
