# coding=utf-8

from django.db import models
from django.contrib.auth.models import User, Group


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
        return self.name


class Bid(models.Model):
    vybor = models.IntegerField(null=True, blank=True)

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

    class Meta:
        verbose_name = "Заявки"
        verbose_name_plural = "Заявки"

    @staticmethod
    def get_queryset(request):
        # str(request.user.groups.values_list('id', flat=True).first())
        query = Bid.objects.filter(groupid=str(request.user.groups.values_list('id', flat=True).first()))
        if request.user.is_superuser:
            query = Bid.objects.all()
        return query

    def __str__(self):
        return "заявка " + str(self.id)


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

    city = models.CharField("Город", blank=True,
                            max_length=128)

    # "Дополнительные данные"

    partner_name = models.CharField("Партнер",
                                    choices=PARTNER_CHOICES,
                                    max_length=32)
    status = models.ForeignKey(BidStatus,
                               verbose_name="Статус заявки",
                               blank=True,
                               null=True, on_delete=models.SET_NULL)
    user_who_edit = models.ForeignKey(User,
                                      verbose_name="Пользователь изменивший эту заявку",
                                      related_name="user_double_bids",
                                      blank=True,
                                      null=True, on_delete=models.SET_NULL)
    created_dt = models.DateTimeField("Дата создания",
                                      auto_now_add=True)
    updated_dt = models.DateTimeField("Дата изменения",
                                      auto_now=True)

    class Meta:
        verbose_name = "Заявка (Дубль)"
        verbose_name_plural = "Заявки (Дубли)"

    @staticmethod
    def get_queryset(request):
        query = BidDouble.objects.filter(groupid=str(request.user.groups.values_list('id', flat=True).first()))
        if request.user.is_superuser:
            query = BidDouble.objects.all()
        return query

    def __str__(self):
        return self.user.username + self.user.last_name + self.user.first_name


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
