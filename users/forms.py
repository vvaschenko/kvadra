# coding=utf-8
import datetime
from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import PasswordInput, SelectDateWidget, ModelForm
from django.contrib.auth.models import User
# from django_auth_ldap.backend import LDAPBackend

from kvadra import settings
# from mon.models import PreferenceMon
from users.models import ProfileUser


# import ldap
# from django_auth_ldap.config import LDAPSearch, PosixGroupType


class Registration(forms.Form):
    username = forms.CharField(max_length=150, error_messages={'required': 'Вы забыли указать имя пользователя'})
    email = forms.EmailField(max_length=254, error_messages={'required': 'Вы забыли указать Email'})
    password = forms.CharField(widget=PasswordInput(), error_messages={'required': 'Вы забыли ввести пароль'})
    repassword = forms.CharField(widget=PasswordInput, error_messages={'required': 'Укажите пароль еще раз'})

    # Валидация проходит в этом методе
    def clean(self):

        if self.cleaned_data.get('password') != self.cleaned_data.get('repassword'):
            raise forms.ValidationError('Пароли должны совпадать!', code='invalid')

        return self.cleaned_data

    def clean_username(self):
        curent_user = self.cleaned_data.get('username')

        if User.objects.filter(username=curent_user).exists():
            raise forms.ValidationError('Пользователь с таким именем уже есть', code='invalid')

        return curent_user

    def clean_email(self):
        curent_email = self.cleaned_data.get('email')

        if User.objects.filter(email=curent_email).exists():
            raise forms.ValidationError('Пользователь с таким email уже есть', code='invalid')

        return curent_email


class Login(forms.Form):
    username = forms.CharField(max_length=150, error_messages={'required': 'Вы забыли указать имя пользователя'})
    password = forms.CharField(widget=PasswordInput(), error_messages={'required': 'Вы забыли ввести пароль'})

    def get_user(self):
        return self.user or None

    def get_password(self):
        return self.password or None

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # print u"Пользователь: %s" % username
        # print u"Пароль: %s" % password
        if not self.errors:
            # ldapauth = LDAPBackend()
            # attrs = []
            # try:
            #
            #     con = ldapauth.ldap.initialize(settings.AUTH_LDAP_SERVER_URI)
            #     con.protocol_version = ldap.VERSION3
            #     con.set_option (ldap.OPT_DEBUG_LEVEL, 1)
            #     con.set_option (ldap.OPT_REFERRALS, 0)
            #     filter = 'uid=%s' % username
            #     result_search = con.search_s('ou=PrivatBank,o=privat', ldap.SCOPE_SUBTREE, filter, attrs)
            #     user_dn = settings.AUTH_LDAP_USER_DN_TEMPLATE % {'user':username}
            #     user_dn_temp = 'vadim.vaschenko@privatbank.ua'
            #     con.simple_bind_s(user_dn,password)
            #
            #     found, data = result_search[0]
            #
            #     count = 0
            #     result_set = []
            #     timeout = 0
            #
            #     # for entry in result_search:
            #     #     try:
            #     #         name = entry[1]['cn'][0].decode("utf-8")
            #     #         # email = entry[1]['mail'][0]
            #     #         phone = entry[1]['telephoneNnumber'][0]
            #     #         desc = entry[1]['description'][0].decode("utf-8")
            #     #         count = count + 1
            #     #         print "%d.\nName: %s\nDescription: %s\nPhone: %s\n" % \
            #     #               (count, name, desc, phone)
            #     #     except:
            #     #         pass
            #
            #     con.unbind()
            # except ldap.INVALID_CREDENTIALS, e:
            #     print e
            # # try:
            # #     dd = ldapauth.authenticate_ldap_user(ldap_user=username,password=password)
            # # except ldap.LDAPError, e:
            # #     print e

            user = authenticate(username=username, password=password)

            if user is None:
                raise forms.ValidationError('Имя пользователя и пароль не подходят', code='invalid')
            self.user = user

        return self.cleaned_data


class ChangePassword(forms.Form):
    password = forms.CharField(widget=PasswordInput(), error_messages={'required': 'Вы забыли ввести пароль'})
    repassword = forms.CharField(widget=PasswordInput, error_messages={'required': 'Укажите пароль еще раз'})

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('repassword'):
            raise forms.ValidationError('Пароли должны совпадать!', code='invalid')

        return self.cleaned_data


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    # avatar = forms.CharField(max_length=1000)
    # birthday = forms.DateInput

    class Meta:
        model = ProfileUser
        fields = ['birthday', 'avatar', 'id_telegram']
        localized_fields = ('birthday',)
        widgets = {
            'birthday': forms.DateInput(format=['%Y-%m-%d']), }

        # def clean_birthday(self):
        #     print u"проверка поля birthday"
        #     curent_birthday = datetime.datetime.strptime(self.data.get('birthday'), '%Y-%m-%d')
        #
        #     print curent_birthday
        #     return curent_birthday
        #

    def clean_avatar(self):
        curent_avatar = self.cleaned_data.get('avatar')
        # print u'проверка поля avatar'
        # print curent_avatar
        return curent_avatar


# class FormDataFields(forms.Field):
class RestPassword(forms.Form):
    username = forms.CharField(max_length=150, error_messages={'required': 'Вы забыли указать имя пользователя'})
    email = forms.EmailField(max_length=254, error_messages={'required': 'Вы забыли указать Email'})

    def clean(self):
        curent_user = self.cleaned_data.get('username')
        curent_email = self.cleaned_data.get('email')
        if User.objects.filter(username=curent_user, email=curent_email).exists():
            pass
        else:
            raise forms.ValidationError('Связка пользователя с email не найдена!', code='invalid')

        return self.cleaned_data


# class Settings(forms.ModelForm):
#     class Meta:
#         model = PreferenceMon
#         fields = '__all__'

class UserEdit(forms.ModelForm):
    class Meta:
        model = ProfileUser
        exclude = ("user", "avatar", "id_telegram", "")

    def __init__(self, *args, **kwargs):
        # status = kwargs.pop(status['code'], None)
        # status = kwargs['instance'].status
        super(UserEdit, self).__init__(*args, **kwargs)
        fields_required = ['first_name', 'last_name']
        for key in self.fields:
            if key not in fields_required:
                self.fields[key].required = False
                print(key)
