# coding=utf-8
from django import forms
from .models import Bid, BidStatus


class BidsAdd(forms.ModelForm):
    class Meta:
        model = Bid
        exclude = ("vybor", "user", "user_who_edit", "created_dt", "updated_dt", "goupid", "is_double")

    def clean_user(self):
        curentuser = self.user
        return curentuser


class BidsEdit(forms.ModelForm):
    class Meta:
        model = Bid
        exclude = ("vybor", "user", "user_who_edit", "created_dt", "updated_dt", "goupid", "is_double")

    def __init__(self, *args, **kwargs):
        self.site_id = kwargs.pop('site_id')
        super(BidsEdit, self).__init__(*args, **kwargs)
        bid = Bid.objects.get(id=self.site_id)
        groups = bid.user.groups.all()
        self.fields["status"].queryset = BidStatus.objects.filter(group__in=groups).distinct()
        fields_required = []
        for key in self.fields:
            if key not in fields_required:
                self.fields[key].required = False

