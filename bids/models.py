# coding=utf-8

from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class BidStatus(models.Model):
    LEVEL_CHOICES = (
        ('1', '1'),
        ('2', '2')
    )
    name = models.CharField("Имя/Название статуса",
                            max_length=128,
                            unique=True)
    code = models.CharField("Код статуса",
                            max_length=128,
                            unique=True)
    level = models.CharField("Уровень вложения", choices=LEVEL_CHOICES, max_length=1)
    parent_level_status = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                            verbose_name="Родительский уровень статуса")
    group = models.ManyToManyField(Group, verbose_name="Группа")

    class Meta:
        verbose_name = "Статус заявки"
        verbose_name_plural = "Статусы заявок"

    def __str__(self):
        if self.parent_level_status is None or self.parent_level_status == "":
            return self.name
        else:
            return self.name


class Bid(models.Model):
    vybor = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Клиент")

    # Дополнительные  телефоны
    number_phone1 = models.CharField("Номер телефона 1", max_length=20, null=True, blank=True)
    cod_number_phone1 = models.CharField("Код телефона 1", max_length=4, null=True, blank=True)

    number_phone2 = models.CharField("Номер телефона 2", max_length=20, null=True, blank=True)
    cod_number_phone2 = models.CharField("Код телефона 2", max_length=4, null=True, blank=True)

    number_phone3 = models.CharField("Номер телефона 3", max_length=20, null=True, blank=True)
    cod_number_phone3 = models.CharField("Код телефона 3", max_length=4, null=True, blank=True)

    number_phone4 = models.CharField("Номер телефона 4", max_length=20, null=True, blank=True)
    cod_number_phone4 = models.CharField("Код телефона 4", max_length=4, null=True, blank=True)

    number_phone5 = models.CharField("Номер телефона 5", max_length=20, null=True, blank=True)
    cod_number_phone5 = models.CharField("Код телефона 5", max_length=4, null=True, blank=True)

    # Мессенджеры
    number_Viber = models.CharField("Номер Viber", max_length=30, null=True, blank=True)

    number_WhatsApp = models.CharField("Номер WhatsApp", max_length=30, null=True, blank=True)

    number_Telegram = models.CharField("Номер Telegram", max_length=30, null=True, blank=True)

    status_Viber = models.CharField("Статус Viber", max_length=255, null=True, blank=True)

    # Трудоустройство
    place_of_work = models.CharField("Місце Роботи", max_length=255, null=True, blank=True)

    position = models.CharField("Посада", max_length=255, null=True, blank=True)

    number_phone_work = models.CharField("Номер телефона рабочий", max_length=20, null=True, blank=True)

    cod_number_phone_work = models.CharField("Код телефона рабочий", max_length=10, null=True, blank=True)

    # Доходы
    income = models.IntegerField("Дохід", null=True, blank=True)

    other_income = models.IntegerField("Інший Дохід", null=True, blank=True)

    family_income = models.IntegerField("Сімейний Дохід", null=True, blank=True)

    total_income = models.IntegerField("Загальний Дохід", null=True, blank=True)

    # "Дополнительные данные"

    name_base = models.CharField("Назва Бази", max_length=255, blank=True)

    remark = models.CharField("Примітка", max_length=255, null=True, blank=True)

    base_id = models.CharField("ID бази", max_length=255, null=True, blank=True)

    name_project = models.CharField("Назва проекту", max_length=255, null=True, blank=True)

    project_id = models.CharField("ID проекту", max_length=255, null=True, blank=True)

    status = models.ForeignKey(BidStatus,
                               verbose_name="Статус заявки",
                               blank=True,
                               null=True, on_delete=models.SET_NULL)
    user_who_edit = models.ForeignKey(User,
                                      verbose_name="Пользователь изменивший эту заявку",
                                      related_name="user_bids",
                                      blank=True,
                                      null=True, on_delete=models.SET_NULL)
    created_dt = models.DateTimeField("Дата создания",
                                      auto_now_add=True)
    updated_dt = models.DateTimeField("Дата изменения",
                                      auto_now=True)
    is_double = models.BooleanField(default=False, verbose_name="Дубль?")

    class Meta:
        verbose_name = "Заявки"
        verbose_name_plural = "Заявки"
        permissions = [('view_bid_double', 'Может видеть дубликаты')]

    def __str__(self):
        return "заявка " + str(self.id) + " " + self.user.username


class BidImport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Клиент")

    # Дополнительные  телефоны
    number_phone1 = models.CharField("Номер телефона 1", max_length=20, null=True, blank=True)
    cod_number_phone1 = models.CharField("Код телефона 1", max_length=4, null=True, blank=True)

    number_phone2 = models.CharField("Номер телефона 2", max_length=20, null=True, blank=True)
    cod_number_phone2 = models.CharField("Код телефона 2", max_length=4, null=True, blank=True)

    number_phone3 = models.CharField("Номер телефона 3", max_length=20, null=True, blank=True)
    cod_number_phone3 = models.CharField("Код телефона 3", max_length=4, null=True, blank=True)

    number_phone4 = models.CharField("Номер телефона 4", max_length=20, null=True, blank=True)
    cod_number_phone4 = models.CharField("Код телефона 4", max_length=4, null=True, blank=True)

    number_phone5 = models.CharField("Номер телефона 5", max_length=20, null=True, blank=True)
    cod_number_phone5 = models.CharField("Код телефона 5", max_length=4, null=True, blank=True)

    # Мессенджеры
    number_Viber = models.CharField("Номер Viber", max_length=30, null=True, blank=True)

    number_WhatsApp = models.CharField("Номер WhatsApp", max_length=30, null=True, blank=True)

    number_Telegram = models.CharField("Номер Telegram", max_length=30, null=True, blank=True)

    status_Viber = models.CharField("Статус Viber", max_length=255, null=True, blank=True)

    # Трудоустройство
    place_of_work = models.CharField("Місце Роботи", max_length=255, null=True, blank=True)

    position = models.CharField("Посада", max_length=255, null=True, blank=True)

    number_phone_work = models.CharField("Номер телефона рабочий", max_length=20, null=True, blank=True)
    cod_number_phone_work = models.CharField("Код телефона рабочий", max_length=10, null=True, blank=True)

    # Доходы
    income = models.IntegerField("Дохід", null=True, blank=True)

    other_income = models.IntegerField("Інший Дохід", null=True, blank=True)

    family_income = models.IntegerField("Сімейний Дохід", null=True, blank=True)

    total_income = models.IntegerField("Загальний Дохід", null=True, blank=True)

    # "Дополнительные данные"
    name_base = models.CharField("Назва Бази", max_length=255, null=True, blank=True)

    remark = models.CharField("Примітка", max_length=255, null=True, blank=True)

    base_id = models.CharField("ID бази", max_length=255, null=True, blank=True)

    name_project = models.CharField("Назва проекту", max_length=255, null=True, blank=True)

    project_id = models.CharField("ID проекту", max_length=255, null=True, blank=True)

    city = models.CharField("Город", max_length=128, null=True, blank=True)

    created_dt = models.DateTimeField("Дата создания",
                                      auto_now_add=True)
    updated_dt = models.DateTimeField("Дата изменения",
                                      auto_now=True)

    class Meta:
        verbose_name = "Импорт завки"
        verbose_name_plural = "Импорт заявок"

    def __str__(self):
        return self.id


class StatusHistory(models.Model):
    new_status = models.ForeignKey(BidStatus, on_delete=models.SET_NULL, null=True, blank=True,
                                   verbose_name="Имя статуса")
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, verbose_name="Заявка")
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.new_status.name + str(self.created_date)

    class Meta:
        verbose_name = "История статусов"
        verbose_name_plural = "История статусов"


@receiver(post_save, sender=Bid)
def create_history(sender, instance, **kwargs):
    print(instance.status)
    history = StatusHistory.objects.create(bid=instance, new_status=instance.status)
    history.save()


@receiver(pre_save, sender=Bid)
def create_history(sender, instance, **kwargs):
    st = StatusHistory.objects.all()
    print(st)
    #st = StatusHistory.objects.filter(bid__id=instance.id).order_by("-created_date")
    try:
        print("change")
        print(st)
        print(st[0].new_status.name)
        print(instance.status.name)
        if len(st) == 0 or st[0].new_status.name != instance.status.name:
            history = StatusHistory.objects.create(bid=instance, new_status=instance.status)
            history.save()
    except:
        print("create_new")
