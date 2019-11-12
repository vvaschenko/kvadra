# coding: utf8
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from users.validators import (
    validate_contact_phone_numeric,
    validate_contact_phone_length,
    validate_passport_series)


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(_(u'avatar'), upload_to='avatar', blank=True, max_length=1000)
    # Добавляем поле дня рождения.
    id_telegram = models.BigIntegerField(null=True, blank=True, default=0)

    # Персональные данные клиента
    first_name = models.CharField("Имя",
                                  max_length=255,
                                  null=True,
                                  blank=True)
    middle_name = models.CharField("Отчество",
                                   max_length=255,
                                   null=True,
                                   blank=True)
    last_name = models.CharField("Фамилия",
                                 max_length=255,
                                 null=True,
                                 blank=True)

    birthday = models.CharField("Дата рождения",
                                max_length=10,
                                # validators=[validate_birthday],
                                null=True,
                                blank=True)
    itn = models.CharField("ИНН",
                           max_length=10,
                           null=True,
                           blank=True)
    email = models.EmailField("Email",
                              null=True,
                              blank=True)
    contact_phone = models.CharField("Номер телефона",
                                     validators=[
                                         validate_contact_phone_numeric,
                                         validate_contact_phone_length
                                     ], null=True, blank=True,
                                     max_length=12)

    # Юридический адрес
    registration_area_ur = models.CharField("Область Реєстрації", max_length=255, null=True, blank=True)

    registration_raion_ur = models.CharField("Район Реєстрації", max_length=255, null=True, blank=True)

    registration_city_ur = models.CharField("Місто Реєстрації", max_length=255, null=True, blank=True)

    registration_street_ur = models.CharField("Вулиця Реєстрації", max_length=255, null=True, blank=True)

    House_number_ur = models.CharField("Номер Будинку Реєстрації", max_length=10, null=True, blank=True)

    apartment_number_ur = models.CharField("Номер Квартири Реєстрації", max_length=10, null=True, blank=True)

    # Фактический адрес

    registration_area_fiz = models.CharField("Область Проживання", max_length=255, null=True, blank=True)

    registration_raion_fiz = models.CharField("Район Проживання", max_length=255, null=True, blank=True)

    registration_city_fiz = models.CharField("Місто Проживання", max_length=255, null=True, blank=True)

    registration_street_fiz = models.CharField("Вулиця Проживання", max_length=255, null=True, blank=True)

    House_number_fiz = models.CharField("Номер Будинку Проживання", max_length=10, null=True, blank=True)

    apartment_number_fiz = models.CharField("Номер Квартири Проживання", max_length=10, null=True, blank=True)

    # Паспорт / ID карта
    passport_series = models.CharField("Серия паспорта",
                                       max_length=16,
                                       validators=[validate_passport_series], null=True,
                                       blank=True)
    passport_number = models.CharField("Номер паспорта",
                                       max_length=32,
                                       blank=True)

    issued_by = models.CharField("Паспорт кем Видано",
                                 max_length=255, null=True,
                                 blank=True)

    date_of_issue = models.DateField("Паспорт Дата Видачі", null=True, blank=True)

    mailing_list = models.BooleanField("Участь в розсилках", default=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return "%s %s %s %s" % (
            self.last_name,
            self.first_name,
            self.middle_name,
            self.user.groups.values_list("name", flat=True)
        )


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileUser.objects.create(user=instance)
    instance.profileuser.save()
