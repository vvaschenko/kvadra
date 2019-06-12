# coding=utf-8
from django import forms
from django.contrib.auth.models import Group

from users.models import ProfileUser
from .models import Bid, BidStatus, BidDouble


class BidsAdd(forms.ModelForm):
    class Meta:
        model = Bid
        exclude = ("partner_name", "lead_id", "webmaster_id", "crm_status", "site_bid_id", "for_skybank", "city")

    fieldsets = [
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
                "mailing_list",
                "remark",
                "base_id",
                "name_project",
                "project_id"
            )
        }),
        ("Информация о заявке", {
            "fields": (
                "user_who_edit"
            )
        })
    ]

    def clean_user(self):
        curentuser = self.user
        return curentuser


class BidsUserAdd(forms.ModelForm):
    class Meta:
        model = ProfileUser
        exclude = ()

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
        })
    ]


class BidsDouble(forms.ModelForm):
    class Meta:
        model = BidDouble
        exclude = ("partner_name", "lead_id", "webmaster_id", "crm_status", "site_bid_id", "for_skybank", "city")

    fieldsets = [
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
                "mailing_list",
                "remark",
                "base_id",
                "name_project",
                "project_id"
            )
        }),
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
        exclude = ("vybor", "user_who_edit", "created_dt", "updated_dt", "site_bid_id", "for_skybank", "city", )

    def clean_status(self):
        curentstatus = BidStatus.objects.get(id=self.cleaned_data['status'].id)
        return curentstatus

    def clean_groupid(self):
        groupid = self.cleaned_data['groupid'].id
        return groupid

    def __init__(self, *args, **kwargs):
        # status = kwargs.pop(status['code'], None)
        # status = kwargs['instance'].status
        super(BidsEdit, self).__init__(*args, **kwargs)
        self.fields['status'] = forms.ModelMultipleChoiceField(queryset=BidStatus.objects.all(), required=False,
                                                               widget=forms.Select(attrs={'class': "form-control"}, ))
        fields_required = []
        for key in self.fields:
            if key not in fields_required:
                self.fields[key].required = False
                print(key)
        # self.fields['groupid'] = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False,
        #                                                        widget=forms.Select(attrs={'class': "form-control"}, ))



class DoubleEdit(forms.ModelForm):
    class Meta:
        model = BidDouble
        exclude = ("partner_name", "lead_id", "webmaster_id", "crm_status", "site_bid_id", "for_skybank", "city")

    # def clean_user(self):
    #     curentuser = self.user
    #     return curentuser

    def clean_status(self):
        curentstatus = BidStatus.objects.get(id=self.cleaned_data['status'].id)
        return curentstatus

    def clean_groupid(self):
        groupid = self.cleaned_data['groupid'].id
        return groupid

    def __init__(self, *args, **kwargs):
        # status = kwargs.pop(status['code'], None)
        # status = kwargs['instance'].status
        super(DoubleEdit, self).__init__(*args, **kwargs)
        self.fields['status'] = forms.ModelChoiceField(queryset=BidStatus.objects.all(), empty_label="Выберите статус",
                                                       required=False,
                                                       widget=forms.Select(attrs={'class': "form-control"}, ))
        self.fields['groupid'] = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False,
                                                                widget=forms.Select(attrs={'class': "form-control"}, ))
