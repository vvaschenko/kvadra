# coding=utf-8
import base64
import re
import requests
import json
from smtplib import SMTPAuthenticationError

from django.contrib import auth, messages
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout

from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from kvadra import settings
# from mon.models import PreferenceMon
from users.forms import Registration, Login, UserForm, ProfileForm, ChangePassword, RestPassword
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.core.mail import EmailMessage
from django.conf import settings as conf_settings


# from utils.client_pubsub import clearcach, link_rs
# from utils.myldapbackend import MyLdapBackend

# server_id = settings.ECA_SERVER_ID
# server_key = settings.ECA_SERVER_KEY
# redirect_uri = settings.ECA_SERVER_REDIRECT_URI
# token_uri = settings.ECA_SERVER_TOKEN_URI
# serv_auth = settings.ECA_SERVER_AUTHORIZE
# serv_user_get = settings.ECA_SERVER_USER_GET
# serv_logout = settings.ECA_SERVER_LOGOUT
# key_link = base64.encodestring(server_id + ':' + server_key).rstrip()
# access_token = ''


@login_required()
def index(request):
    # if request.method == 'GET':
    #     print 'метод GET'
    #     if request.user.is_authenticated():
    #         print 'Пользователь %s авторизовван' % request.user
    #     else:
    #         print 'Пользователь %s не авторизовван' % request.user
    #         return render(request, 'mon/login.html', locals())
    #
    # if request.method == 'POST':
    #     print 'метод POST'
    #     print request.user
    #

    return HttpResponseRedirect('/login/')


def guest(request):
    return render(request, 'users/guest.html', locals())


def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            if form.get_user():
                # print "user: %s" % form.get_user()
                auth.login(request, form.get_user())
                return HttpResponseRedirect('/bids/bids/')
                # return HttpResponseRedirect('users/guest.html')
    else:
        form = Login()

    return render(request, 'users/login.html', {'form': form})


#
# def mylogin(request):
#     global server_id, server_key, key_link, access_token, error_er, error_desc
#     urlname = request.GET.get('next', None)
#     code_auth = request.GET.get('code', None)
#     remember_me = request.GET.get('remember_me', None)
#
#     expires_in = 0
#     context = {}
#     if request.method == 'POST':
#         form = Login(request.POST)
#         if form.is_valid():
#             if form.get_user():
#                 # print "user: %s" % form.get_user()
#                 ################################
#                 ################################
#
#                 auth.login(request, form.get_user())
#                 for group in request.user.groups.values_list():
#                     if (u'guest' in group):
#                         context["guest"] = 1
#                         request.session.set_expiry(1200)
#                         break
#                 if urlname is None:
#                     return HttpResponseRedirect('/mon/monitor/')
#                 else:
#                     return HttpResponseRedirect(urlname)
#     else:
#
#         if code_auth is None:
#             return HttpResponseRedirect(
#                 serv_auth + '?client_id=' + server_id + '&scope=read&response_type=code&state=enter&nonce=' + server_key + '&redirect_uri=' + redirect_uri)
#         else:
#             headers = {'Authorization': 'Basic ' + key_link}
#             post_data = {'grant_type': 'authorization_code',
#                          'code': code_auth,
#                          'nonce': server_key,
#                          'redirect_uri': redirect_uri}
#
#             response = requests.post(token_uri, post_data, headers=headers,
#                                      verify=False)
#             content = response.content
#             prob_str = re.sub("^\s+|\n|\r|\s+$", '', content)
#             if 'error' in prob_str:
#                 access_token = None
#                 error_desc = json.loads(prob_str)['error_description']
#                 error_er = json.loads(prob_str)['error']
#             else:
#                 access_token = json.loads(prob_str)['access_token']
#                 expires_in = json.loads(prob_str)['expires_in']
#             if access_token is not None:
#                 key_token = access_token
#                 headers = {'Authorization': 'Bearer ' + key_token}
#                 post_data = {'format': 'json',
#                              'nonce': server_key}
#                 response = requests.get(serv_user_get, post_data, headers=headers,
#                                         verify=False)
#                 content = response.content
#                 prob_str = re.sub("^\s+|\n|\r|\s+$", '', content)
#                 username = json.loads(prob_str)['username']
#                 mybackauth = MyLdapBackend()
#                 user = mybackauth.authenticate(username)
#                 login(request, mybackauth.get_user(user.id))
#                 request.session.set_expiry(expires_in)
#                 for group in request.user.groups.values_list():
#                     if (u'guest' in group):
#                         context["guest"] = 1
#                         request.session.set_expiry(1200)
#                         break
#                     else:
#                         # request.session.set_expiry(180)
#                         request.session.set_expiry(expires_in)
#             else:
#                 logout(request)
#                 return HttpResponse('Return an invalid login error message.</br>%s %s' % (error_er, error_desc))
#                 # return render(request, 'users/error_auth.html', {'error_er':error_er, 'error_desc':error_desc }, locals())
#
#     return HttpResponseRedirect('/mon/monitor/')
#     #         # return render(request, 'mon/monitor.html', post_data)
#     #
#     #         # form = Login()
#     #
#     # return render(request, 'users/login.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        # Если форма прошла валидацию
        if form.is_valid():
            cd = form.cleaned_data
            new_user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            group = Group.objects.get_or_create(name='guest')[0]
            new_user.is_staff = True
            # new_user.is_staff = False
            new_user.groups.add(group)
            new_user.save()
            group.save()

            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect('/bids/bids/')
                else:
                    return HttpResponse('Return a disabled account error message')
            else:
                return HttpResponse('Return an invalid login error message.')

    else:
        form = Registration()

    return render(request, 'users/registr.html', {'form': form})


def log_out(request):
    if 'back' in request.POST:
        return HttpResponseRedirect('/bids/bids/')
    elif 'log_out' in request.POST:
        auth.logout(request)
        return HttpResponseRedirect('/')

    return render(request, 'users/logout.html', locals())


# def log_out(request):
#     global server_id, server_key, key_link, access_token, redirect_uri, serv_logout
#     if 'back' in request.POST:
#         return HttpResponseRedirect('/')
#     elif 'log_out' in request.POST:
#         logout(request)
#         key_token = access_token
#         headers = {'Authorization': 'Bearer ' + key_token}
#         # post_data = {'client_id': server_id,'scope': 'read','start_uri': redirect_uri}
#
#         post_data = {'nonce': server_key
#                      }
#         response = requests.post(serv_logout, post_data, headers=headers,
#                                  verify=False)
#         content = response.content
#         prob_str = re.sub("^\s+|\n|\r|\s+$", '', content)
#         if prob_str == '':
#             redirect_uri = redirect_uri
#         else:
#             redirect_uri = json.loads(prob_str)['redirect_uri']
#         return HttpResponseRedirect(redirect_uri)
#
#     return render(request, 'users/logout.html', locals())


@login_required()
@transaction.atomic
def profile(request):
    # , {"p_query": posts}
    # context = RequestContext(request)
    context = {}
    context["timeobr"] = datetime.strftime(datetime.now(), "%A, %d. %B %Y %I:%M%p")
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)

        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profileuser)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return HttpResponseRedirect('/users/profile/')
            # return redirect('users/profile.html')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profileuser)

    # context["user_form"] = user_form.initial

    return render(request, 'users/profile.html',
                  {'timeobr': datetime.strftime(datetime.now(), "%A, %d. %B %Y %I:%M%p"), 'user_form': user_form,
                   'profile_form': profile_form})


@login_required()
def change_password(request):
    if request.method == 'POST':
        form = ChangePassword(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            u = User.objects.get(username=request.user)
            u.set_password(cd['password'])
            u.save()
            update_session_auth_hash(request, u)
            return HttpResponseRedirect('/bids/bids/')
    else:
        form = ChangePassword()

    return render(request, 'users/change_password.html', {'form': form})


def rest_password(request):
    if request.method == 'POST':
        form = RestPassword(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = cd['username']
            mail = cd['email']
            newpaswd = User.objects.make_random_password()
            u = User.objects.get(username=user)
            u.set_password(newpaswd)
            u.save()
            subject = 'kvadra - сброс пароля'
            body = u'Вы запросили сброс пароля для сервера kvadra \n' \
                   u'новый пароль - %s' % newpaswd

            mail_from = conf_settings.EMAIL_HOST_USER  # ваш аккааунт
            mail_to = [mail]  # список получателей

            mail = EmailMessage(subject, body, mail_from, mail_to)
            mail.content_subtype = "html"
            try:
                mail.send(fail_silently=False)
            except (SMTPAuthenticationError) as exc:
                print('Error send mail')

            return HttpResponseRedirect('/users/login/')
    else:
        form = RestPassword()

    return render(request, 'users/rest_password.html', {'form': form})

#
# @login_required()
# def settings(request):
#     results = dict()
#     results['success'] = False
#     results['otvet'] = " "
#     my_settings = PreferenceMon.objects.first()
#     my_settings.ase_psw = base64.decodestring(my_settings.ase_psw)
#     my_settings.rs_psw = base64.decodestring(my_settings.rs_psw)
#     my_settings.delay_psw_user_delay = base64.decodestring(my_settings.delay_psw_user_delay)
#     if request.method == 'POST':
#         form = Settings(request.POST, instance=my_settings)
#         if form.is_valid():
#             cd = form.cleaned_data
#             # form.ase_psw = base64.encodestring(cd['ase_psw'])
#             my_settings.ase_psw = base64.encodestring(cd['ase_psw'])
#             my_settings.rs_psw = base64.encodestring(cd['rs_psw'])
#             my_settings.delay_psw_user_delay = base64.encodestring(cd['delay_psw_user_delay'])
#             my_settings.dsirestart = cd['dsirestart']
#             form.save()
#             my_settings.save()
#             messages.success(request, _('Your settings was successfully updated!'))
#             return HttpResponseRedirect('/mon/monitor/')
#             # return redirect('users/profile.html')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#
#     else:
#         form = Settings(instance=my_settings)
#     if request.is_ajax() and request.method == 'POST':
#         cach = request.POST.get('cach', None)
#         linkrs = request.POST.get('linkrs', None)
#         if cach == '1':
#             otv_cach = clearcach()
#             results['otvet'] = otv_cach
#             results['success'] = True
#         else:
#             results['otvet'] = ""
#             results['success'] = False
#
#         if linkrs == '1':
#             otv_linkrs = link_rs()
#             results['otvet'] = otv_linkrs
#             results['success'] = True
#         else:
#             results['otvet'] = ""
#             results['success'] = False
#         return JsonResponse(results)
#
#     return render(request, 'users/settings.html', {'form': form})
