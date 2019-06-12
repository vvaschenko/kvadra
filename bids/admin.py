# coding=utf-8
from django.contrib import admin
from bids.models import *


@admin.register(BidStatus)
class BidStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    tabs = True
    #list_display = ('last_name',
    #                'first_name',
    #                'contact_phone',
    #                'status',
    #                'created_dt')
    fieldsets = [
        ("Клиент", {
            "fields": [
                ("user",)
            ]
        }),
        ("Телефоны", {
            "fields": [
                ("cod_number_phone1", "number_phone1"),
                ("cod_number_phone2", "number_phone2"),
                ("cod_number_phone3", "number_phone3"),
                ("cod_number_phone4", "number_phone4"),
                ("cod_number_phone5", "number_phone5")
            ]
        }),
        ("Мессенджеры", {
            "fields": (
                "number_Viber",
                "number_WhatsApp",
                "number_Telegram",
                "status_Viber"
            )
        }),
        ("Трудоустройство", {
            "fields": (
                "place_of_work",
                "position",
                "number_phone_work",
                "cod_number_phone_work"
            )
        }),
        ("Доходы", {
            "fields": (
                "income",
                "other_income",
                "family_income",
                "total_income"
            )
        }),
        ("Дополнительные данные", {
            "fields": (
                "name_base",
                "remark",
                "base_id",
                "name_project",
                "project_id"
            )
        }),
        ("Информация о заявке", {
            "fields": (
                # "partner_name",
                "user_who_edit",
            )
        })
    ]


@admin.register(BidImport)
class BidImportAdmin(admin.ModelAdmin):
    tabs = True
#    list_display = ('last_name',
#                    'first_name',
#                    'contact_phone',
#                    # 'status',
#                    'created_dt')
    fieldsets = [
        ("Клиент", {
            "fields": [
                ("user",)
            ]
        }),
        ("Телефоны", {
            "fields": [
                ("cod_number_phone1", "number_phone1"),
                ("cod_number_phone2", "number_phone2"),
                ("cod_number_phone3", "number_phone3"),
                ("cod_number_phone4", "number_phone4"),
                ("cod_number_phone5", "number_phone5")
            ]
        }),
        ("Мессенджеры", {
            "fields": (
                "number_Viber",
                "number_WhatsApp",
                "number_Telegram",
                "status_Viber"
            )
        }),
        ("Трудоустройство", {
            "fields": (
                "place_of_work",
                "position",
                "number_phone_work",
                "cod_number_phone_work"
            )
        }),
        ("Доходы", {
            "fields": (
                "income",
                "other_income",
                "family_income",
                "total_income"
            )
        }),
        ("Дополнительные данные", {
            "fields": (
                "name_base",
                "remark",
                "base_id",
                "name_project",
                "project_id"
            )
        })
    ]


@admin.register(BidDouble)
class BidDoubleAdmin(admin.ModelAdmin):
    tabs = True
#    list_display = ('last_name',
#                    'first_name',
#                    'contact_phone',
#                   'created_dt')
    fieldsets = [
        ("Клиент", {
            "fields": [
                ("user",)
            ]
        }),
        ("Телефоны", {
            "fields": [
                ("cod_number_phone1", "number_phone1"),
                ("cod_number_phone2", "number_phone2"),
                ("cod_number_phone3", "number_phone3"),
                ("cod_number_phone4", "number_phone4"),
                ("cod_number_phone5", "number_phone5")
            ]
        }),
        ("Мессенджеры", {
            "fields": (
                "number_Viber",
                "number_WhatsApp",
                "number_Telegram",
                "status_Viber"
            )
        }),
        ("Трудоустройство", {
            "fields": (
                "place_of_work",
                "position",
                "number_phone_work",
                "cod_number_phone_work"
            )
        }),
        ("Доходы", {
            "fields": (
                "income",
                "other_income",
                "family_income",
                "total_income"
            )
        }),
        ("Дополнительные данные", {
            "fields": (
                "name_base",
                "remark",
                "base_id",
                "name_project",
                "project_id"
            )
        }),
        ("Информация о заявке", {
            "fields": (
                # "partner_name",
                "user_who_edit",
            )
        })
    ]

