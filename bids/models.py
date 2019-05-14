# coding=utf-8


# from simple_history import register


from django.db import models
from django.contrib.auth.models import User

# from sources.models import renamed_path
# from departments.models import Department, Appointment
# from .helpers import check_blacklist, get_tomorrow


from .validators import (validate_birthday,
                         validate_contact_phone_numeric,
                         validate_contact_phone_length,
                         validate_passport_series)


class BidStatus(models.Model):
    name = models.CharField("Имя/Название статуса",
                            max_length=128,
                            unique=True)
    code = models.CharField("Код статуса",
                            max_length=128,
                            unique=True)

    class Meta:
        verbose_name = "Статус заявки"
        verbose_name_plural = "Статусы заявок"

    def __str__(self):
        return self.name


class Bid(models.Model):
    PARTNER_CHOICES = (
        ('easysoft', 'EasySoft(EasyPay)'),
        ('admitad', 'Admitad'),
        ('salesdoubler', 'Salesdoubler'),
        ('website', 'Website'),
        ('doaffiliate', 'Doaffiliate'),
        ('linkprofit', 'Linkprofit'),
        ('hotline', 'HotLine'),
        ('treeum', 'Treeum'),
        ('turnes', 'Turnes'),
        ('recommendation', 'Рекомендация'),
        ('lifecell', 'Lifecell'),
        ('city24', 'City24')
    )

    partner_name = models.CharField("Партнер",
                                    choices=PARTNER_CHOICES,
                                    max_length=32)
    lead_id = models.IntegerField("ID клиента",
                                  blank=True,
                                  null=True)
    webmaster_id = models.CharField("Webmaster ID",
                                    max_length=32,
                                    blank=True)

    credit_sum = models.IntegerField("Сумма кредита",
                                     blank=True,
                                     null=True)
    # Персональные данные клиента

    first_name = models.CharField("Имя",
                                  max_length=255,
                                  blank=True)
    middle_name = models.CharField("Отчество",
                                   max_length=255,
                                   blank=True)
    last_name = models.CharField("Фамилия",
                                 max_length=255,
                                 blank=True)

    birthday = models.CharField("Дата рождения",
                                max_length=10,
                                # validators=[validate_birthday],
                                blank=True)
    itn = models.CharField("ИНН",
                           max_length=10,
                           blank=True)
    email = models.EmailField("Email",
                              blank=True)
    contact_phone = models.CharField("Номер телефона",
                                     validators=[
                                         validate_contact_phone_numeric,
                                         validate_contact_phone_length
                                     ],
                                     max_length=12)
    # Дополнительные  телефоны
    number_phone1 = models.CharField("Номер телефона 1", max_length=20, blank=True)
    cod_number_phone1 = models.CharField("Код телефона 1", max_length=4, blank=True)

    number_phone2 = models.CharField("Номер телефона 2", max_length=20, blank=True)
    cod_number_phone2 = models.CharField("Код телефона 2", max_length=4, blank=True)

    number_phone3 = models.CharField("Номер телефона 3", max_length=20, blank=True)
    cod_number_phone3 = models.CharField("Код телефона 3", max_length=4, blank=True)

    number_phone4 = models.CharField("Номер телефона 4", max_length=20, blank=True)
    cod_number_phone4 = models.CharField("Код телефона 4", max_length=4, blank=True)

    number_phone5 = models.CharField("Номер телефона 5", max_length=20, blank=True)
    cod_number_phone5 = models.CharField("Код телефона 5", max_length=4, blank=True)

    # Мессенджеры
    number_Viber = models.CharField("Номер Viber", max_length=30, blank=True)

    number_WhatsApp = models.CharField("Номер WhatsApp", max_length=30, blank=True)

    number_Telegram = models.CharField("Номер Telegram", max_length=30, blank=True)

    status_Viber = models.CharField("Статус Viber", max_length=255, blank=True)

    # Трудоустройство
    place_of_work = models.CharField("Місце Роботи", max_length=255, blank=True)

    position = models.CharField("Посада", max_length=255, blank=True)

    number_phone_work = models.CharField("Номер телефона рабочий", max_length=20, blank=True)
    cod_number_phone_work = models.CharField("Код телефона рабочий", max_length=10, blank=True)

    # Доходы
    income = models.IntegerField("Дохід", blank=True)

    other_income = models.IntegerField("Інший Дохід", blank=True)

    family_income = models.IntegerField("Сімейний Дохід", blank=True)

    total_income = models.IntegerField("Загальний Дохід", blank=True)

    # Юридический адрес
    registration_area_ur = models.CharField("Область Реєстрації", max_length=255, blank=True)

    registration_raion_ur = models.CharField("Район Реєстрації", max_length=255, blank=True)

    registration_city_ur = models.CharField("Місто Реєстрації", max_length=255, blank=True)

    registration_street_ur = models.CharField("Вулиця Реєстрації", max_length=255, blank=True)

    House_number_ur = models.CharField("Номер Будинку Реєстрації", max_length=10, blank=True)

    apartment_number_ur = models.CharField("Номер Квартири Реєстрації", max_length=10, blank=True)

    # Фактический адрес

    registration_area_fiz = models.CharField("Область Проживання", max_length=255, blank=True)

    registration_raion_fiz = models.CharField("Район Проживання", max_length=255, blank=True)

    registration_city_fiz = models.CharField("Місто Проживання", max_length=255, blank=True)

    registration_street_fiz = models.CharField("Вулиця Проживання", max_length=255, blank=True)

    House_number_fiz = models.CharField("Номер Будинку Проживання", max_length=10, blank=True)

    apartment_number_fiz = models.CharField("Номер Квартири Проживання", max_length=10, blank=True)

    # Паспорт / ID карта
    passport_series = models.CharField("Серия паспорта",
                                       max_length=16,
                                       validators=[validate_passport_series],
                                       blank=True)
    passport_number = models.CharField("Номер паспорта",
                                       max_length=32,
                                       blank=True)

    issued_by = models.CharField("Паспорт Ким Видано",
                                 max_length=255,
                                 blank=True)

    date_of_issue = models.DateField("Паспорт Дата Видачі", null=True)

    # "Дополнительные данные"
    name_base = models.CharField("Назва Бази", max_length=255, blank=True)

    mailing_list = models.CharField("Участь в розсилках", max_length=255, blank=True)

    remark = models.CharField("Примітка", max_length=255, blank=True)

    base_id = models.CharField("ID бази", max_length=255, blank=True)

    name_project = models.CharField("Назва проекту", max_length=255, blank=True)

    project_id = models.CharField("ID проекту", max_length=255, blank=True)

    city = models.CharField("Город",
                            max_length=128)

    status = models.ForeignKey(BidStatus,
                               verbose_name="Статус заявки",
                               blank=True,
                               null=True)
    # crm_status = models.CharField("CRM status",
    #                               max_length=32,
    #                               blank=True)
    user = models.ForeignKey(User,
                             verbose_name="Пользователь изменивший эту заявку",
                             related_name="user_bids",
                             blank=True,
                             null=True)
    created_dt = models.DateTimeField("Дата создания",
                                      auto_now_add=True)
    updated_dt = models.DateTimeField("Дата изменения",
                                      auto_now=True)

    # site_bid_id = models.IntegerField(
    #     "ID заявки на сайте expressfinance",
    #     blank=True,
    #     null=True
    # )

    # for_skybank = models.BooleanField(
    #     "Передано на Skybank",
    #     default=False
    # )

    # department = models.ForeignKey(
    #     Department,
    #     verbose_name="Отделение",
    #     blank=True,
    #     null=True
    # )
    # appointment_dt = models.DateTimeField(
    #     "Дата встречи с клиентом",
    #     blank=True,
    #     null=True
    # )
    # appointment = models.OneToOneField(
    #     Appointment,
    #     verbose_name="Встреча",
    #     related_name="appointment_bid",
    #     blank=True,
    #     null=True
    # )
    groupid = models.IntegerField("ID группы",
                                  blank=True,
                                  null=True)

    class Meta:
        verbose_name = "Заявки"
        verbose_name_plural = "Заявки"

    # def save(self, *args, **kwargs):
    #     if self.user.is_superuser:
    #         # userid = User(id=self.user_id)
    #         # if userid is None:
    #         #     self.groupid = str(0)
    #         # else:
    #         #     self.groupid = str(userid.groups.values_list('id', flat=True).first())
    #         pass
    #     else:
    #         self.groupid = str(self.user.groups.values_list('id', flat=True).first())
    #
    #     super(Bid, self).save(*args, **kwargs)

    @staticmethod
    def get_queryset(request):
        # str(request.user.groups.values_list('id', flat=True).first())
        query = Bid.objects.filter(groupid=str(request.user.groups.values_list('id', flat=True).first()))
        if request.user.is_superuser:
            query = Bid.objects.all()
        return query

    def __str__(self):
        return "{} {}".format(self.partner_name, self.city)



class BidDouble(models.Model):
    PARTNER_CHOICES = (
        ('easysoft', 'EasySoft(EasyPay)'),
        ('admitad', 'Admitad'),
        ('salesdoubler', 'Salesdoubler'),
        ('website', 'Website'),
        ('doaffiliate', 'Doaffiliate'),
        ('linkprofit', 'Linkprofit'),
        ('hotline', 'HotLine'),
        ('treeum', 'Treeum'),
        ('turnes', 'Turnes'),
        ('recommendation', 'Рекомендация'),
        ('lifecell', 'Lifecell'),
        ('city24', 'City24')
    )

    partner_name = models.CharField("Партнер",
                                    choices=PARTNER_CHOICES,
                                    max_length=32)
    lead_id = models.IntegerField("ID клиента",
                                  blank=True,
                                  null=True)
    webmaster_id = models.CharField("Webmaster ID",
                                    max_length=32,
                                    blank=True)

    credit_sum = models.IntegerField("Сумма кредита",
                                     blank=True,
                                     null=True)
    # Персональные данные клиента

    first_name = models.CharField("Имя",
                                  max_length=255,
                                  blank=True)
    middle_name = models.CharField("Отчество",
                                   max_length=255,
                                   blank=True)
    last_name = models.CharField("Фамилия",
                                 max_length=255,
                                 blank=True)

    birthday = models.CharField("Дата рождения",
                                max_length=10,
                                # validators=[validate_birthday],
                                blank=True)
    itn = models.CharField("ИНН",
                           max_length=10,
                           blank=True)
    email = models.EmailField("Email",
                              blank=True)
    contact_phone = models.CharField("Номер телефона",
                                     validators=[
                                         validate_contact_phone_numeric,
                                         validate_contact_phone_length
                                     ],
                                     max_length=12)
    # Дополнительные  телефоны
    number_phone1 = models.CharField("Номер телефона 1", max_length=20, blank=True)
    cod_number_phone1 = models.CharField("Код телефона 1", max_length=4, blank=True)

    number_phone2 = models.CharField("Номер телефона 2", max_length=20, blank=True)
    cod_number_phone2 = models.CharField("Код телефона 2", max_length=4, blank=True)

    number_phone3 = models.CharField("Номер телефона 3", max_length=20, blank=True)
    cod_number_phone3 = models.CharField("Код телефона 3", max_length=4, blank=True)

    number_phone4 = models.CharField("Номер телефона 4", max_length=20, blank=True)
    cod_number_phone4 = models.CharField("Код телефона 4", max_length=4, blank=True)

    number_phone5 = models.CharField("Номер телефона 5", max_length=20, blank=True)
    cod_number_phone5 = models.CharField("Код телефона 5", max_length=4, blank=True)

    # Мессенджеры
    number_Viber = models.CharField("Номер Viber", max_length=30, blank=True)

    number_WhatsApp = models.CharField("Номер WhatsApp", max_length=30, blank=True)

    number_Telegram = models.CharField("Номер Telegram", max_length=30, blank=True)

    status_Viber = models.CharField("Статус Viber", max_length=255, blank=True)

    # Трудоустройство
    place_of_work = models.CharField("Місце Роботи", max_length=255, blank=True)

    position = models.CharField("Посада", max_length=255, blank=True)

    number_phone_work = models.CharField("Номер телефона рабочий", max_length=20, blank=True)
    cod_number_phone_work = models.CharField("Код телефона рабочий", max_length=10, blank=True)

    # Доходы
    income = models.IntegerField("Дохід", null=True, default=0)

    other_income = models.IntegerField("Інший Дохід", null=True, default=0)

    family_income = models.IntegerField("Сімейний Дохід", null=True, default=0)

    total_income = models.IntegerField("Загальний Дохід", null=True, default=0)

    # Юридический адрес
    registration_area_ur = models.CharField("Область Реєстрації", max_length=255, blank=True)

    registration_raion_ur = models.CharField("Район Реєстрації", max_length=255, blank=True)

    registration_city_ur = models.CharField("Місто Реєстрації", max_length=255, blank=True)

    registration_street_ur = models.CharField("Вулиця Реєстрації", max_length=255, blank=True)

    House_number_ur = models.CharField("Номер Будинку Реєстрації", max_length=10, blank=True)

    apartment_number_ur = models.CharField("Номер Квартири Реєстрації", max_length=10, blank=True)

    # Фактический адрес

    registration_area_fiz = models.CharField("Область Проживання", max_length=255, blank=True)

    registration_raion_fiz = models.CharField("Район Проживання", max_length=255, blank=True)

    registration_city_fiz = models.CharField("Місто Проживання", max_length=255, blank=True)

    registration_street_fiz = models.CharField("Вулиця Проживання", max_length=255, blank=True)

    House_number_fiz = models.CharField("Номер Будинку Проживання", max_length=10, blank=True)

    apartment_number_fiz = models.CharField("Номер Квартири Проживання", max_length=10, blank=True)

    # Паспорт / ID карта
    passport_series = models.CharField("Серия паспорта",
                                       max_length=16,
                                       validators=[validate_passport_series],
                                       blank=True)
    passport_number = models.CharField("Номер паспорта",
                                       max_length=32,
                                       blank=True)

    issued_by = models.CharField("Паспорт Ким Видано",
                                 max_length=255,
                                 blank=True)

    date_of_issue = models.DateField("Паспорт Дата Видачі", null=True)

    # "Дополнительные данные"
    name_base = models.CharField("Назва Бази", max_length=255, blank=True)

    mailing_list = models.CharField("Участь в розсилках", max_length=255, blank=True)

    remark = models.CharField("Примітка", max_length=255, blank=True)

    base_id = models.CharField("ID бази", max_length=255, blank=True)

    name_project = models.CharField("Назва проекту", max_length=255, blank=True)

    project_id = models.CharField("ID проекту", max_length=255, blank=True)

    city = models.CharField("Город",
                            max_length=128)

    status = models.ForeignKey(BidStatus,
                               verbose_name="Статус заявки",
                               blank=True,
                               null=True)
    # crm_status = models.CharField("CRM status",
    #                               max_length=32,
    #                               blank=True)
    user = models.ForeignKey(User,
                             verbose_name="Пользователь изменивший эту заявку",
                             blank=True,
                             null=True)
    created_dt = models.DateTimeField("Дата создания",
                                      auto_now_add=True)
    updated_dt = models.DateTimeField("Дата изменения",
                                      auto_now=True)

    # site_bid_id = models.IntegerField(
    #     "ID заявки на сайте expressfinance",
    #     blank=True,
    #     null=True
    # )
    #
    # for_skybank = models.BooleanField(
    #     "Передано на Skybank",
    #     default=False
    # )

    # department = models.ForeignKey(
    #     Department,
    #     verbose_name="Отделение",
    #     blank=True,
    #     null=True
    # )
    # appointment_dt = models.DateTimeField(
    #     "Дата встречи с клиентом",
    #     blank=True,
    #     null=True
    # )
    # appointment = models.OneToOneField(
    #     Appointment,
    #     verbose_name="Встреча",
    #     related_name="appointment_biddouble",
    #     blank=True,
    #     null=True
    # )
    groupid = models.IntegerField("ID группы",
                                  blank=True,
                                  null=True)

    class Meta:
        verbose_name = "Заявка (Дубль)"
        verbose_name_plural = "Заявки (Дубли)"

    # def save(self, *args, **kwargs):
    #     if self.user.is_superuser:
    #         # userid = User(id=self.user_id)
    #         # if userid is None:
    #         #     self.groupid = str(0)
    #         # else:
    #         #     self.groupid = str(userid.groups.values_list('id', flat=True).first())
    #         pass
    #     else:
    #         self.groupid = str(self.user.groups.values_list('id', flat=True).first())
    #
    #     super(BidDouble, self).save(*args, **kwargs)


    @staticmethod
    def get_queryset(request):
        # str(request.user.groups.values_list('id', flat=True).first())
        query = BidDouble.objects.filter(groupid=str(request.user.groups.values_list('id', flat=True).first()))
        if request.user.is_superuser:
            query = BidDouble.objects.all()
        return query

    def __str__(self):
        return "{} {}".format(self.partner_name, self.city)


class BidImport(models.Model):
    partner_name = models.CharField("Партнер", max_length=32)
    lead_id = models.IntegerField("ID клиента",
                                  blank=True,
                                  null=True)
    webmaster_id = models.CharField("Webmaster ID",
                                    max_length=32,
                                    blank=True)

    credit_sum = models.IntegerField("Сумма кредита",
                                     blank=True,
                                     null=True)
    # Персональные данные клиента

    first_name = models.CharField("Имя",
                                  max_length=255,
                                  blank=True)
    middle_name = models.CharField("Отчество",
                                   max_length=255,
                                   blank=True)
    last_name = models.CharField("Фамилия",
                                 max_length=255,
                                 blank=True)

    birthday = models.CharField("Дата рождения",
                                max_length=10,
                                # validators=[validate_birthday],
                                blank=True)
    itn = models.CharField("ИНН",
                           max_length=10,
                           blank=True)
    email = models.EmailField("Email",
                              blank=True)
    contact_phone = models.CharField("Номер телефона",
                                     # validators=[
                                     #     validate_contact_phone_numeric,
                                     #     validate_contact_phone_length
                                     # ],
                                     max_length=12)
    # Дополнительные  телефоны
    number_phone1 = models.CharField("Номер телефона 1", max_length=20, blank=True)
    cod_number_phone1 = models.CharField("Код телефона 1", max_length=4, blank=True)

    number_phone2 = models.CharField("Номер телефона 2", max_length=20, blank=True)
    cod_number_phone2 = models.CharField("Код телефона 2", max_length=4, blank=True)

    number_phone3 = models.CharField("Номер телефона 3", max_length=20, blank=True)
    cod_number_phone3 = models.CharField("Код телефона 3", max_length=4, blank=True)

    number_phone4 = models.CharField("Номер телефона 4", max_length=20, blank=True)
    cod_number_phone4 = models.CharField("Код телефона 4", max_length=4, blank=True)

    number_phone5 = models.CharField("Номер телефона 5", max_length=20, blank=True)
    cod_number_phone5 = models.CharField("Код телефона 5", max_length=4, blank=True)

    # Мессенджеры
    number_Viber = models.CharField("Номер Viber", max_length=30, blank=True)

    number_WhatsApp = models.CharField("Номер WhatsApp", max_length=30, blank=True)

    number_Telegram = models.CharField("Номер Telegram", max_length=30, blank=True)

    status_Viber = models.CharField("Статус Viber", max_length=255, blank=True)

    # Трудоустройство
    place_of_work = models.CharField("Місце Роботи", max_length=255, blank=True)

    position = models.CharField("Посада", max_length=255, blank=True)

    number_phone_work = models.CharField("Номер телефона рабочий", max_length=20, blank=True)
    cod_number_phone_work = models.CharField("Код телефона рабочий", max_length=10, blank=True)

    # Доходы
    income = models.IntegerField("Дохід", null=True, default=0)

    other_income = models.IntegerField("Інший Дохід", null=True, default=0)

    family_income = models.IntegerField("Сімейний Дохід", null=True, default=0)

    total_income = models.IntegerField("Загальний Дохід", null=True, default=0)

    # Юридический адрес
    registration_area_ur = models.CharField("Область Реєстрації", max_length=255, blank=True)

    registration_raion_ur = models.CharField("Район Реєстрації", max_length=255, blank=True)

    registration_city_ur = models.CharField("Місто Реєстрації", max_length=255, blank=True)

    registration_street_ur = models.CharField("Вулиця Реєстрації", max_length=255, blank=True)

    House_number_ur = models.CharField("Номер Будинку Реєстрації", max_length=10, blank=True)

    apartment_number_ur = models.CharField("Номер Квартири Реєстрації", max_length=10, blank=True)

    # Фактический адрес

    registration_area_fiz = models.CharField("Область Проживання", max_length=255, blank=True)

    registration_raion_fiz = models.CharField("Район Проживання", max_length=255, blank=True)

    registration_city_fiz = models.CharField("Місто Проживання", max_length=255, blank=True)

    registration_street_fiz = models.CharField("Вулиця Проживання", max_length=255, blank=True)

    House_number_fiz = models.CharField("Номер Будинку Проживання", max_length=10, blank=True)

    apartment_number_fiz = models.CharField("Номер Квартири Проживання", max_length=10, blank=True)

    # Паспорт / ID карта
    passport_series = models.CharField("Серия паспорта",
                                       max_length=16,
                                       # validators=[validate_passport_series],
                                       blank=True)
    passport_number = models.CharField("Номер паспорта",
                                       max_length=32,
                                       blank=True)

    issued_by = models.CharField("Паспорт Ким Видано",
                                 max_length=255,
                                 blank=True)

    date_of_issue = models.DateField("Паспорт Дата Видачі", null=True)

    # "Дополнительные данные"
    name_base = models.CharField("Назва Бази", max_length=255, blank=True)

    mailing_list = models.CharField("Участь в розсилках", max_length=255, blank=True)

    remark = models.CharField("Примітка", max_length=255, blank=True)

    base_id = models.CharField("ID бази", max_length=255, blank=True)

    name_project = models.CharField("Назва проекту", max_length=255, blank=True)

    project_id = models.CharField("ID проекту", max_length=255, blank=True)

    city = models.CharField("Город",
                            max_length=128)

    # status = models.ForeignKey(BidStatus,
    #                            verbose_name="Статус заявки",
    #                            blank=True,
    #                            null=True)
    # crm_status = models.CharField("CRM status",
    #                               max_length=32,
    #                               blank=True)
    # user = models.ForeignKey(User,
    #                          verbose_name="Пользователь изменивший эту заявку",
    #                          blank=True,
    #                          null=True)
    created_dt = models.DateTimeField("Дата создания",
                                      auto_now_add=True)
    updated_dt = models.DateTimeField("Дата изменения",
                                      auto_now=True)

    # site_bid_id = models.IntegerField(
    #     "ID заявки на сайте kvadraonline",
    #     blank=True,
    #     null=True
    # )
    #
    # for_skybank = models.BooleanField(
    #     "Передано на Skybank",
    #     default=False
    # )
    groupid = models.IntegerField("ID группы",
                                  blank=True,
                                  null=True)

    # department = models.ForeignKey(
    #     Department,
    #     verbose_name="Отделение",
    #     blank=True,
    #     null=True
    # )
    # appointment_dt = models.DateTimeField(
    #     "Дата встречи с клиентом",
    #     blank=True,
    #     null=True
    # )
    # appointment = models.OneToOneField(
    #     Appointment,
    #     verbose_name="Встреча",
    #     related_name="appointment_bid",
    #     blank=True,
    #     null=True
    # )

    class Meta:
        verbose_name = "Импорт завки"
        verbose_name_plural = "Импорт заявок"
    #
    # def save(self, *args, **kwargs):
    #     if self.partner_name != 'turnes':
    #         person_in_blacklist = check_blacklist(      # Examples:
    #             itn=self.itn,                           # 9342830297
    #             passseria=self.passport_series,         # TK
    #             passnumber=self.passport_number,        # 085108
    #             mobile_phone=self.contact_phone[2:]     # 0991110077
    #         )
    #
    #         # least one object exists, set status to current Bid
    #         if person_in_blacklist:
    #             blacklist_status = BidStatus.objects.filter(code=666)
    #             if blacklist_status:
    #                 self.status = blacklist_status[0]
    #
    #     super(Bid, self).save(*args, **kwargs)
    #
    # def __str__(self):
    #     return "{} {}".format(self.partner_name, self.city)

# Register models for track history of changes

# register(Bid, cascade_delete_history=True)
