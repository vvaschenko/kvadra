# coding=utf-8
from django import forms
from .models import Bid, BidStatus


class BidsAdd(forms.ModelForm):
    class Meta:
        model = Bid
        exclude = ("partner_name", "lead_id", "webmaster_id", "crm_status", "site_bid_id", "for_skybank", "city")

    fieldsets = [
        ("Клиент", {
            "fields": [
                "contact_phone",
                "last_name",
                "first_name",
                "middle_name",
                "itn",
                # ("passport_series", "passport_number"),
                "birthday",
                # "city",
                # "credit_sum",
                "email"
                # "status"
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
        ("Юр. адрес", {
            "fields": (
                "registration_area_ur",
                "registration_raion_ur",
                "registration_city_ur",
                "registration_street_ur",
                "House_number_ur",
                "apartment_number_ur"
            )
        }),
        ("Фактический адрес", {
            "fields": (
                "registration_area_fiz",
                "registration_raion_fiz",
                "registration_city_fiz",
                "registration_street_fiz",
                "House_number_fiz",
                "apartment_number_fiz"
            )
        }),
        ("Паспорт / ID карта", {
            "fields": (
                ("passport_series", "passport_number"),
                "issued_by",
                "date_of_issue"
            )
        }),
        ("Дополнительные данные", {
            "fields": (
                "name_base",
                "mailing_list",
                "remark",
                "base_id",
                "name_project",
                "project_id"
            )
        }),
        # ("Отделение", {
        #     "fields": (
        #         "department",
        #         "appointment_dt",
        #         "appointment"
        #     )
        # }),
        ("Информация о заявке", {
            "fields": (
                # "partner_name",
                # "lead_id",
                # "webmaster_id",
                # "crm_status",
                "user"
                # "site_bid_id",
                # "for_skybank"
            )
        })
    ]

    def clean_user(self):
        curentuser = self.user
        return curentuser


class BidDouble(forms.ModelForm):
    class Meta:
        model = Bid
        exclude = ("partner_name", "lead_id", "webmaster_id", "crm_status", "site_bid_id", "for_skybank", "city")

    fieldsets = [
        ("Клиент", {
            "fields": [
                "contact_phone",
                "last_name",
                "first_name",
                "middle_name",
                "itn",
                # ("passport_series", "passport_number"),
                "birthday",
                # "city",
                # "credit_sum",
                "email"
                # "status"
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
        ("Юр. адрес", {
            "fields": (
                "registration_area_ur",
                "registration_raion_ur",
                "registration_city_ur",
                "registration_street_ur",
                "House_number_ur",
                "apartment_number_ur"
            )
        }),
        ("Фактический адрес", {
            "fields": (
                "registration_area_fiz",
                "registration_raion_fiz",
                "registration_city_fiz",
                "registration_street_fiz",
                "House_number_fiz",
                "apartment_number_fiz"
            )
        }),
        ("Паспорт / ID карта", {
            "fields": (
                ("passport_series", "passport_number"),
                "issued_by",
                "date_of_issue"
            )
        }),
        ("Дополнительные данные", {
            "fields": (
                "name_base",
                "mailing_list",
                "remark",
                "base_id",
                "name_project",
                "project_id"
            )
        }),
        # ("Отделение", {
        #     "fields": (
        #         "department",
        #         "appointment_dt",
        #         "appointment"
        #     )
        # }),
        ("Информация о заявке", {
            "fields": (
                # "partner_name",
                # "lead_id",
                # "webmaster_id",
                # "crm_status",
                "user"
                # "site_bid_id",
                # "for_skybank"
            )
        })
    ]

    def clean_user(self):
        curentuser = self.user
        return curentuser


class BidsEdit(forms.ModelForm):
    class Meta:
        model = Bid
        exclude = ("partner_name", "lead_id", "webmaster_id", "crm_status", "site_bid_id", "for_skybank", "city")


    # status = forms.ModelChoiceField(queryset=BidStatus.objects.values_list('name', flat=True),
    #                                 to_field_name='code',
    #                                 empty_label="Выберите статус")
    # widget=forms.Select(
    #     attrs={'class': "form-control", 'onchange': 'showqueryalert(id)', }))

    fieldsets = [
        ("Клиент", {
            "fields": [
                "contact_phone",
                "last_name",
                "first_name",
                "middle_name",
                "itn",
                # ("passport_series", "passport_number"),
                "birthday",
                # "city",
                # "credit_sum",
                "email",
                "status"
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
        ("Юр. адрес", {
            "fields": (
                "registration_area_ur",
                "registration_raion_ur",
                "registration_city_ur",
                "registration_street_ur",
                "House_number_ur",
                "apartment_number_ur"
            )
        }),
        ("Фактический адрес", {
            "fields": (
                "registration_area_fiz",
                "registration_raion_fiz",
                "registration_city_fiz",
                "registration_street_fiz",
                "House_number_fiz",
                "apartment_number_fiz"
            )
        }),
        ("Паспорт / ID карта", {
            "fields": (
                ("passport_series", "passport_number"),
                "issued_by",
                "date_of_issue"
            )
        }),
        ("Дополнительные данные", {
            "fields": (
                "name_base",
                "mailing_list",
                "remark",
                "base_id",
                "name_project",
                "project_id"
            )
        }),
        # ("Отделение", {
        #     "fields": (
        #         "department",
        #         "appointment_dt",
        #         "appointment"
        #     )
        # }),
        ("Информация о заявке", {
            "fields": (
                # "partner_name",
                # "lead_id",
                # "webmaster_id",
                # "crm_status",
                "user"
                # "site_bid_id",
                # "for_skybank"
            )
        })
    ]

    def clean_user(self):
        curentuser = self.user
        return curentuser

    def __init__(self, *args, **kwargs):
        # status = kwargs.pop(status['code'], None)
        status = kwargs['instance'].status
        super(BidsEdit, self).__init__(*args, **kwargs)
        if status:
            self.fields['status'] = forms.ModelChoiceField(
                queryset=BidStatus.objects.values_list('name', flat=True),
                # to_field_name='name',
                initial={'status': int(status.code)},
                empty_label="Выберите статус",
                widget=forms.Select(
                    attrs={'class': "form-control", })
            )
            self.fields['status'].required = False
        else:
            self.fields['status'] = forms.ModelChoiceField(
                queryset=BidStatus.objects.values_list('name', flat=True),
                to_field_name='code',
                # initial={'status': 0},
                empty_label="Выберите статус",
                widget=forms.Select(
                    attrs={'class': "form-control", })
            )

            self.fields['status'].required = False


class DoubleEdit(forms.ModelForm):
    class Meta:
        model = Bid
        exclude = ("partner_name", "lead_id", "webmaster_id", "crm_status", "site_bid_id", "for_skybank", "city")

    fieldsets = [
        ("Клиент", {
            "fields": [
                "contact_phone",
                "last_name",
                "first_name",
                "middle_name",
                "itn",
                # ("passport_series", "passport_number"),
                "birthday",
                # "city",
                # "credit_sum",
                "email"
                "status"
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
        ("Юр. адрес", {
            "fields": (
                "registration_area_ur",
                "registration_raion_ur",
                "registration_city_ur",
                "registration_street_ur",
                "House_number_ur",
                "apartment_number_ur"
            )
        }),
        ("Фактический адрес", {
            "fields": (
                "registration_area_fiz",
                "registration_raion_fiz",
                "registration_city_fiz",
                "registration_street_fiz",
                "House_number_fiz",
                "apartment_number_fiz"
            )
        }),
        ("Паспорт / ID карта", {
            "fields": (
                ("passport_series", "passport_number"),
                "issued_by",
                "date_of_issue"
            )
        }),
        ("Дополнительные данные", {
            "fields": (
                "name_base",
                "mailing_list",
                "remark",
                "base_id",
                "name_project",
                "project_id"
            )
        }),
        # ("Отделение", {
        #     "fields": (
        #         "department",
        #         "appointment_dt",
        #         "appointment"
        #     )
        # }),
        ("Информация о заявке", {
            "fields": (
                # "partner_name",
                # "lead_id",
                # "webmaster_id",
                # "crm_status",
                "user"
                # "site_bid_id",
                # "for_skybank"
            )
        })
    ]

    def clean_user(self):
        curentuser = self.user
        return curentuser
