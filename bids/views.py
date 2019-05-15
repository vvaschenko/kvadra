# coding=utf-8
from time import sleep

import xlrd
import json
import logging

from datetime import datetime, time
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from dateutil.tz import tzutc, tzlocal, struct
from django.views.generic import View, TemplateView
from django.http import Http404, JsonResponse, HttpResponseRedirect
from everbug.utils.serilalize import _

from bids.forms import BidsAdd, BidDouble, BidsEdit, DoubleEdit
from bids.utils import list_name_tuple, get_key, get_value_excel
# from questionnaires.models import ShortQuestionnaire, Verification
from .models import Bid, BidImport, BidDouble, BidStatus

log = logging.getLogger(__name__)
tzutc = tzutc()
tzlocal = tzlocal()


@login_required
def bids(request):
    context = {}
    results = dict()
    results['success'] = False
    max_datetime = {'datatime__max': datetime.now(tzlocal)}
    if request.method == 'POST':
        del_id = request.POST.get('id', None)
        del_delite = request.POST.get('delite', None)
        if del_delite == '1':
            delstr = del_id.find('_')
            idfordel = int(del_id[delstr + 1:])
            try:
                Bid.objects.get(id=idfordel).delete()
                results['success'] = True
            except Bid.DoesNotExist:
                log.error(u'Запись не найдена')
        return JsonResponse(results)

    if request.user.is_superuser:
        qs_bids = Bid.objects.select_related().all()
    else:
        qs_bids = Bid.objects.filter(
            groupid=str(request.user.groups.values_list('id', flat=True).first())).select_related().all()
    # m = Membership.objects.filter(person__name='x').values('person', 'person__phonenumber')
    context = {'p_bids': qs_bids}
    context['timeobr'] = datetime.strftime(datetime.astimezone(max_datetime['datatime__max'], tzlocal),
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
        bids_form.user = request.user
        dict_str['itn'] = bids_form.data['itn']
        dict_str['passport_series'] = bids_form.data['passport_series']
        dict_str['passport_number'] = bids_form.data['passport_number']

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
                    messages.error(request, _('Please correct the error below.'))
            except Exception as wwww:
                print(wwww)
            print(qwe)
    else:
        bids_form = BidsAdd()
    return render(request, 'bids/bids_add.html',
                  {'timeobr': datetime.strftime(datetime.now(), "%A, %d. %B %Y %I:%M%p"), 'bids_form': bids_form})


@login_required
def doubleedit(request):
    edit_id = request.GET.get('edit_id', None)
    edit_id = request.GET.get('edit_id', None)
    if edit_id is None:
        return HttpResponseRedirect('/bids/bidsdouble/')
    else:
        qs_bids = BidDouble.objects.get(id=edit_id)
        bids_form = DoubleEdit(instance=qs_bids)

        if request.POST:
            bids_form = DoubleEdit(request.POST)
            if bids_form.is_valid():
                bids_form.save()
            return HttpResponseRedirect('/bids/bidsdouble/')

        return render(request, 'bids/doubleedit.html', {'bids_form': bids_form})



@login_required
def bidsedit(request, edit_id=None):
    context = {}
    max_datetime = {'datatime__max': datetime.now(tzlocal)}
    edit_id = request.GET.get('edit_id', None)
    if edit_id is None:
        return HttpResponseRedirect('/bids/bids/')
    else:

        if request.POST:
            bids_form = BidsEdit(request.POST)
            if bids_form.is_valid():
                bids_form.save()
            return HttpResponseRedirect('/bids/bids/')
        else:
            qs_bids = Bid.objects.get(id=edit_id)
            bids_form = BidsEdit(instance=qs_bids)

        return render(request, 'bids/bids_edit.html', {'bids_form': bids_form})
    # if request.method == 'POST':
    #     regim = request.POST.get('regim', None)
    #     edit_id = request.POST.get('edit_id', None)
    #     bids_form = BidsEdit(request.POST)
    #     if bids_form.is_valid():
    #         bids_form.save()
    #         return HttpResponseRedirect('/bids/bids/')
    #     else:
    #         pass
    #     # if regim == 'double':
    #     #     qs_bids = BidDouble.objects.select_related().get(id=edit_id)
    #     #     bids_form = DoubleEdit(request.POST, instance=qs_bids)
    #     context['success'] = False
    #     # context = {'bids_form': bids_form}
    #     # context['timeobr'] = datetime.strftime(datetime.astimezone(max_datetime['datatime__max'], tzlocal),
    #     #                                        "%Y-%m-%d %H:%M:%S")
    #     return render(request, 'bids/bids_edit.html',
    #                   {'timeobr': datetime.strftime(datetime.now(), "%A, %d. %B %Y %I:%M%p"), 'bids_form': bids_form})

# else:
#     return HttpResponseRedirect('/bids/bids/')


@login_required
def bidsdouble(request, edit_id=None):
    results = dict()
    results['success'] = False
    max_datetime = {'datatime__max': datetime.now(tzlocal)}
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

    if request.user.is_superuser:
        qs_bids = BidDouble.objects.select_related().all()
    else:
        qs_bids = BidDouble.objects.filter(
            groupid=str(request.user.groups.values_list('id', flat=True).first())).select_related().all()
    context = {'p_bids': qs_bids}
    context['timeobr'] = datetime.strftime(datetime.astimezone(max_datetime['datatime__max'], tzlocal),
                                           "%Y-%m-%d %H:%M:%S")
    return render(request, 'bids/bids_double.html', context)


@login_required
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
