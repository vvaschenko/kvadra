# coding=utf-8
from time import sleep

import xlrd
import json
import logging

import datetime
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import Group, User
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from dateutil.tz import tzutc, tzlocal
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from bids.forms import BidsAdd, DoubleEdit, BidsEdit
from bids.utils import list_name_tuple, get_key, get_value_excel
from users.forms import UserEdit
from users.models import ProfileUser
from .models import Bid, BidImport, BidDouble, BidStatus

log = logging.getLogger(__name__)
tzutc = tzutc()
tzlocal = tzlocal()


@login_required
def bids(request):
    context = {}
    results = dict()
    results['success'] = False
    max_datetime = {'datatime__max': datetime.datetime.now(tzlocal)}
    posts = Group.objects.all()
    context["grouplist"] = posts
    if request.method == 'POST':
        del_id = request.POST.get('id', None)
        del_delite = request.POST.get('delite', None)
        zp_id = request.POST.get('zp_id', None)
        regim = request.POST.get('regim', None)
        workbids = request.POST.get('workbids', None)
        stime = request.POST.get('starttime', None)
        etime = request.POST.get('endtime', None)
        filterbids = request.POST.get('filterbids', None)
        proekt = request.POST.get('proekt', None)
        if filterbids is not None:
            if filterbids == '1':
                starttime = datetime.datetime.strptime(stime, "%d.%m.%Y")
                endtime = datetime.datetime.strptime(etime, "%d.%m.%Y")

                qs_bids = Bid.objects.select_related().filter(created_dt__range=[starttime, endtime]).all()
                results['success'] = True
                return JsonResponse(results)
        if regim == 'bids_check':
            bids_zp = Bid.objects.get(id=zp_id)
            bids_zp.vybor = workbids
            try:
                bids_zp.save()
                results['success'] = True
            except:
                log.error(u'Ошибка записи в базу')
            return JsonResponse(results)
        if regim == 'migration_bids':
            try:
                Bid.objects.filter(vybor=1).update(vybor=0)
                results['success'] = True
            except Exception as err:
                log.error(u'Ошибка миграции проекта')
                results['success'] = False
            return JsonResponse(results)

        if del_delite == '1':
            delstr = del_id.find('_')
            idfordel = int(del_id[delstr + 1:])
            try:
                Bid.objects.get(id=idfordel).delete()
                results['success'] = True
            except Bid.DoesNotExist:
                log.error(u'Запись не найдена')
            return JsonResponse(results)
    qs_bids = Bid.objects.select_related().all()
    context['timeobr'] = datetime.datetime.strftime(
        datetime.datetime.astimezone(max_datetime['datatime__max'], tzlocal),
        "%Y-%m-%d %H:%M:%S")
    return render(request, 'bids/bids.html', context)

    # @staticmethod
    # def get_queryset(request):
    #     # str(request.user.groups.values_list('id', flat=True).first())
    #     query = Bid.objects.filter(groupid=str(request.user.groups.values_list('id', flat=True).first()))
    #     if request.user.is_superuser:
    #         query = Bid.objects.all()
    #     return query


@login_required
def bidsadd(request):
    if request.method == 'POST':
        # if request.is_ajax() and request.method == 'POST':
        dict_str = {}
        bids_form = BidsAdd(request.POST)
        bids_user_form = UserEdit(request.POST)
        bids_form.user = request.user
        dict_str['itn'] = bids_user_form.data['itn']
        dict_str['passport_series'] = bids_user_form.data['passport_series']
        dict_str['passport_number'] = bids_user_form.data['passport_number']

        try:
            Bid.objects.get(itn=dict_str['itn'], passport_series=dict_str['passport_series'],
                            passport_number=dict_str['passport_number'])
            try:
                # BidDouble.objects.create(**bids_form.cleaned_data)
                obj = BidDouble.objects.create(**bids_form.cleaned_data)

                obj.save()
                return HttpResponseRedirect('/bids/bidsdouble')
            except Exception as qqq:
                print(qqq)
        except (Bid.DoesNotExist, Exception) as qwe:
            try:
                if bids_form.is_valid():
                    try:
                        bids_form.save()
                        return HttpResponseRedirect('/bids/bids')
                    except Exception as err:
                        print(err)
                else:
                    messages.error(request, 'Please correct the error below.')
            except Exception as wwww:
                print(wwww)
            print(qwe)
    else:
        bids_form = BidsAdd()
        bids_user_form = UserEdit()

    return render(request, 'bids/bids_add.html',
                  {'timeobr': datetime.datetime.strftime(datetime.datetime.now(), "%A, %d. %B %Y %I:%M%p"),
                   'bids_form': bids_form, 'bids_user_form': bids_user_form})


@login_required
def doubleedit(request):
    edit_id = request.GET.get('edit_id', None)
    if edit_id is None:
        return HttpResponseRedirect('/bids/bidsdouble/')
    else:
        # qs_bids = BidDouble.objects.get(id=edit_id)
        bid_double_obj = BidDouble.objects.get(id=edit_id)
        user = bid_double_obj.user.id
        user_obj = ProfileUser.objects.get(user=user)
        groups = user_obj.user.groups.values_list('name', flat=True)
        bids_form = DoubleEdit(instance=bid_double_obj)
        if request.POST:
            bids_form = DoubleEdit(request.POST, instance=BidDouble.objects.get(id=edit_id))
            # bids_form = DoubleEdit(request.POST)
            try:
                if bids_form.is_valid():
                    bids_form.save()
                    return HttpResponseRedirect('/bids/bidsdouble/')
            except Exception as err:
                print(err)

        return render(request, 'bids/doubleedit.html', {'bids_form': bids_form, 'groups': groups})


# done
@login_required
def bidsedit(request):
    edit_id = request.GET.get('edit_id', None)
    if edit_id is None:
        return HttpResponseRedirect('/bids/bids/')
    else:
        bid_obj = Bid.objects.get(id=edit_id)
        user = bid_obj.user.id
        user_obj = ProfileUser.objects.get(user=user)
        groups = user_obj.user.groups.values_list('name', flat=True)
        status_first_level = BidStatus.objects.filter(level='1')
        status_second_level = BidStatus.objects.filter(level='2')
        select_status = bid_obj.status
        if request.method == 'POST':
            bids_form = BidsEdit(request.POST, instance=bid_obj)
            bids_user_form = UserEdit(request.POST, instance=ProfileUser.objects.get(user=user))
            # print(bids_form.errors)
            # print(bids_user_form.errors)

            if bids_form.is_valid() and bids_user_form.is_valid():
                print(bids_form)
                bids_form.save()
                bids_user_form.save()
                # status = request.POST.get('status-list')
                # Bid.objects.get(id=edit_id).update(status=BidStatus.objects.get(id=status))
                return HttpResponseRedirect('/bids/bids/')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            bids_form = BidsEdit(instance=bid_obj)
            bids_user_form = UserEdit(instance=ProfileUser.objects.get(user=user))
        return render(request, 'bids/bids_edit.html', {'bids_form': bids_form, 'bids_user_form': bids_user_form,
                                                       'groups': groups, "f_status": status_first_level,
                                                       "s_status": status_second_level,
                                                       "select_status": select_status})


def user_can_see_double(user):
    group_perm = User.get_group_permissions(user)
    return user.has_perm("bids.view_biddouble") or "bids.view_biddouble" in group_perm


@login_required
@user_passes_test(user_can_see_double)
def bidsdouble(request):
    results = dict()
    results['success'] = False
    max_datetime = {'datatime__max': datetime.datetime.now(tzlocal)}
    if request.method == 'POST':
        del_id = request.POST.get('id', None)
        del_delite = request.POST.get('delite', None)
        if del_delite == '1':
            delstr = del_id.find('_')
            idfordel = int(del_id[delstr + 1:])
            try:
                BidDouble.objects.get(id=idfordel).delete()
                results['success'] = True
            except Bid.DoesNotExist:
                log.error(u'Запись не найдена')
        return JsonResponse(results)

    qs_bids = BidDouble.objects.select_related().all()
    context = {'p_bids': qs_bids, 'timeobr': datetime.datetime.strftime(
        datetime.datetime.astimezone(max_datetime['datatime__max'], tzlocal),
        "%Y-%m-%d %H:%M:%S")}
    return render(request, 'bids/bids_double.html', context)


def user_can_see_import(user):
    group_perm = User.get_group_permissions(user)
    return user.has_perm("bids.view_bidimport") or "bids.view_bidimport" in group_perm


@login_required
@user_passes_test(user_can_see_import)
def bidsimport(request):
    context = {}
    results = dict()
    results['success'] = False
    results['otvet'] = " "
    list_column_name = {}
    list_name = {}
    posts = Group.objects.all()
    context = {"grouplist": posts}
    if request.is_ajax() and request.method == 'POST':
        regim = request.POST.get('regim', None)
        group_id = request.POST.get('idgroup', None)
        # curentuser_id = request.user.id
        # curentuser = request.user

        # if request.FILES['import_bids']:
        if regim is not None:
            if regim == 'readfields':
                # try:

                # except MultiValueDictKeyError as err:
                #     results['success'] = False
                #     results['error'] = 'Ошибка чтения файла, перегрузите страницу и выберите заново'
                #     return JsonResponse(results)
                try:
                    filename = request.FILES['import_bids'].read()
                    book = xlrd.open_workbook(file_contents=filename)
                except MultiValueDictKeyError as err:
                    results['success'] = False
                    results['error'] = 'Ошибка чтения файла, перегрузите страницу и выберите заново'
                    return JsonResponse(results)
                for sheet in book.sheets():
                    number_of_rows = sheet.nrows
                    number_of_columns = sheet.ncols
                    for item in range(0, number_of_columns):
                        list_column_name[item] = (sheet.cell(0, item).value)

                book.release_resources()
                del book

                results['success'] = True
                results['fields_name_db'] = list_name_tuple()
                results['fields_name'] = list_column_name
                return JsonResponse(results)
            if regim == 'import':
                dss = BidImport.objects.all()
                dss.delete()
                # try:
                #     filename = request.FILES['import_bids'].read()
                # except MultiValueDictKeyError as err:
                #     results['success'] = False
                #     results['error'] = 'Ошибка чтения файла, перегрузите страницу и выберите заново'
                #     return JsonResponse(results)
                filename = request.FILES['import_bids'].read()
                list_table = json.loads(request.POST.get('list_table', None))
                bachlist = {}
                bachlist2 = []
                number_of_rows = 0
                number_of_columns = 0
                book = xlrd.open_workbook(file_contents=filename)
                for sheet in book.sheets():
                    number_of_rows = sheet.nrows
                    number_of_columns = sheet.ncols
                    for item in range(0, number_of_columns):
                        list_column_name[item] = (sheet.cell(0, item).value)

                for item_rows in range(1, number_of_rows):
                    for lineitem in range(0, number_of_columns):
                        for poledb in list_table.values():
                            if poledb == list_column_name[lineitem]:
                                name_pole_db = get_key(list_table, poledb)
                                bachlist[name_pole_db] = get_value_excel(book, sheet, item_rows, lineitem)
                    # bachlist["groupid"] = str(request.user.groups.values_list('id', flat=True).first())
                    bachlist["groupid"] = group_id
                    # bachlist["user_id"] = curentuser_id
                    # bachlist["user"] = curentuser
                    if 'itn' in bachlist:
                        if bachlist['itn'].isdigit():
                            pass
                        else:
                            results['success'] = False
                            results['error'] = 'ИНН должен быть заполнен'
                            return JsonResponse(results)
                    else:
                        results['success'] = False
                        results['error'] = 'ИНН должен быть заполнен'
                        return JsonResponse(results)
                    if 'passport_series' in bachlist:
                        pass
                    else:
                        results['success'] = False
                        results['error'] = 'Поле серия паспорта должно быть заполнено'
                        return JsonResponse(results)
                    if 'passport_number' in bachlist:
                        pass
                    else:
                        results['success'] = False
                        results['error'] = 'Поле номер паспорта должно быть заполнено'
                        return JsonResponse(results)

                    # print(bachlist)
                    try:
                        # import_db = BidImport.objects.create(**bachlist)
                        if len(bachlist) > 0:
                            obj = BidImport.objects.create(**bachlist)
                            obj.save()
                        results['success'] = True
                    except Exception as err:
                        results['success'] = False
                        results['error'] = err
                        print(err)
                        return JsonResponse(results)

                book.release_resources()
                del book
                count_dubl = 0
                for stroka in BidImport.objects.all():
                    dict_str = stroka.__dict__
                    del dict_str['_state']
                    # del dict_str['_user_cache']
                    # dict_str['user'] = curentuser
                    try:
                        # Bid.objects.get(**dict_str)
                        Bid.objects.get(itn=dict_str['itn'], passport_series=dict_str['passport_series'],
                                        passport_number=dict_str['passport_number'])
                        obj = BidDouble.objects.create(**dict_str)
                        obj.save()
                        count_dubl += 1
                    except Bid.DoesNotExist:
                        obj = Bid.objects.create(**dict_str)
                        obj.save()

                # return render(request, 'bids/bids_import.html', context)
                results['count_dubl'] = count_dubl
            else:
                pass
            # else:
            #     results['success'] = False
            #     results['error'] = 'Ошибка чтения файла, перегрузите страницу и выберите заново'
            return JsonResponse(results)
    return render(request, 'bids/bids_import.html', context)
