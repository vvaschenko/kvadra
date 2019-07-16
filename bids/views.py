# coding=utf-8
import xlrd
import json
import logging

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group, User
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib import messages
from django.shortcuts import render
from dateutil.tz import tzutc
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.generic import ListView

from bids.forms import BidsAdd, BidsEdit
from bids.utils import list_name_tuple, get_key, get_value_excel
from users.forms import UserEdit, UserAdd
from users.models import ProfileUser
from .models import Bid, BidImport, StatusHistory, BidStatus

log = logging.getLogger(__name__)
tzutc = tzutc()


def user_can_see_double(user):
    group_perm = User.get_group_permissions(user)
    return user.has_perm("bids.view_bid_double") or "bids.view_bid_double" in group_perm


class BidView(ListView):
    template_name = 'bids/bids.html'
    model = Bid

    def get(self, *args, **kwargs):
        link = self.request.get_full_path()
        if link.endswith("/bidsdouble/") and not user_can_see_double(self.request.user):
            return HttpResponseRedirect('../../login/')
        return super(BidView, self).get(*args, **kwargs)

    def post(self, request):
        del_id = request.POST.get('id', None)
        group_id = self.request.POST.getlist('group_id[]', None)
        print(del_id)
        bid_arr = self.request.POST.getlist('bid_id_arr[]', None)
        if del_id is not None:
            try:
                Bid.objects.get(id=del_id).delete()
            except Bid.DoesNotExist:
                log.error(u'Запись не найдена')
        elif group_id is not None and group_id != []:
            try:
                for item in bid_arr:
                    bid_item = Bid.objects.get(id=int(item))
                    bid_item.user.groups.clear()
                    for gr in group_id:
                        bid_item.user.groups.add(Group.objects.get(id=int(gr)))
                    bid_item.save()
            except Exception:
                log.error(u'Ошибка миграции проекта')
            return HttpResponse(status=201)
        return HttpResponse(status=201)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        link = self.request.get_full_path()
        user = self.request.user
        user_groups = user.groups.all()
        context["user_group_list"] = user_groups
        if link.endswith("/bids/"):
            all_bids = Bid.objects.select_related().filter(is_double=False)
            p_bids = []
            for bid in all_bids:
                gr = bid.user.groups.all()
                if gr & user_groups:
                    p_bids.append(bid)
            context["p_bids"] = p_bids
        elif link.endswith("/bidsdouble/"):
            all_bids = Bid.objects.select_related().filter(is_double=True)
            p_bids = []
            for bid in all_bids:
                gr = bid.user.groups.all()
                if gr & user_groups:
                    p_bids.append(bid)
            context["p_bids"] = p_bids
        else:
            context["p_bids"] = Bid.objects.select_related().all()
        context["group_list"] = Group.objects.all()
        return context

    def get_queryset(self, **kwargs):
        link = self.request.get_full_path()
        if link.endswith("/bids/"):
            return Bid.objects.select_related().filter(is_double=False)
        elif link.endswith("/bidsdouble/"):
            return Bid.objects.select_related().filter(is_double=True)
        return Bid.objects.all()


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
        group_list = user_obj.user.groups.all()
        selected_status = bid_obj.status
        f_status = BidStatus.objects.filter(group__in=group_list, level=1).distinct()
        if selected_status is not None and selected_status.level == "2":
            s_status = BidStatus.objects.filter(group__in=group_list, parent_level_status=selected_status.parent_level_status,
                                                level=2).distinct()
        else:
            s_status = BidStatus.objects.filter(group__in=group_list,
                                                parent_level_status=selected_status,
                                                level=2).distinct()
        if request.method == 'POST':
            f_choosed = request.POST.get('f-status-list', None)
            s_choosed = request.POST.get('s-status-list', None)
            if s_choosed is not None and s_choosed != "None":
                status = BidStatus.objects.get(id=s_choosed)
            elif f_choosed is not None:
                status = BidStatus.objects.get(id=f_choosed)
            else:
                status = None
            bids_user_form = UserEdit(request.POST, instance=ProfileUser.objects.get(user=user))
            bids_form = BidsEdit(request.POST, instance=bid_obj, site_id=edit_id)
            # print(bids_user_form.errors)
            # print(bids_form.errors)

            if bids_form.is_valid() and bids_user_form.is_valid():
                bid = bids_form.save(commit=False)
                bid.status = BidStatus.objects.get(id=2)
                bid.user_who_edit = request.user
                bid.status = status
                bid.save()
                bids_user_form.save()
                return HttpResponseRedirect('/bids/bids/')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            bids_form = BidsEdit(instance=bid_obj, site_id=edit_id)
            bids_user_form = UserEdit(instance=ProfileUser.objects.get(user=user))
        return render(request, 'bids/bids_edit.html', {'bids_form': bids_form, 'bids_user_form': bids_user_form,
                                                       'groups': groups,
                                                       "f_status": f_status,
                                                       "s_status": s_status,
                                                       "selected_status": selected_status})


def select_status(request):
    edit_id = request.GET.get('edit_id')
    bid_obj = Bid.objects.get(id=edit_id)
    user = bid_obj.user.id
    user_obj = ProfileUser.objects.get(user=user)
    group_list = user_obj.user.groups.all()
    selected_status = request.GET.get('status_id')
    s_status = BidStatus.objects.filter(group__in=group_list, parent_level_status=selected_status, level=2).distinct()
    return render(request, 'bids/status_dropdown_list_options.html', {'s_status': s_status})


def add_select_status(request):
    selected_status = request.GET.get('status_id')
    s_status = BidStatus.objects.filter(parent_level_status=selected_status, level=2).distinct()
    return render(request, 'bids/status_dropdown_list_options.html', {'s_status': s_status})


@login_required
def bidsadd(request):
    f_status = BidStatus.objects.filter(level=1).distinct()

    if request.method == 'POST':
        bids_form = BidsAdd(request.POST)
        bids_user_form = UserAdd(request.POST)
        bids_form.user = request.user


        itn = bids_user_form.data['itn']
        passport_series = bids_user_form.data['passport_series']
        passport_number = bids_user_form.data['passport_number']

        f_choosed = request.POST.get('f-status-list', None)
        s_choosed = request.POST.get('s-status-list', None)
        if s_choosed is not None and s_choosed != "None":
            status = BidStatus.objects.get(id=s_choosed)
        elif f_choosed is not None:
            status = BidStatus.objects.get(id=f_choosed)
        else:
            status = None
        try:
            prof = ProfileUser.objects.get(itn=itn, passport_series=passport_series,
                                           passport_number=passport_number)
        except:
            username = "U_" + str(itn) + str(passport_series) + str(passport_number)
            u_email = bids_user_form.data['email']
            if u_email is None or u_email == "":
                u_email = "U_" + str(itn) + str(passport_series) + str(passport_number) + "@kvadra.com"
            passport_number = "password1029"
            param = {"username": username, "email": u_email, "password": passport_number}
            user = User.objects.create(**param)
            user.save()
            prof = bids_user_form.save(commit=False)
            prof.user = user
            prof.save()
        bid = Bid.objects.filter(user=prof.user)
        if len(bid) > 0:
            obj = bids_form.save(commit=False)
            obj.user = prof.user
            obj.is_double = True
            group = Group.objects.get_or_create(name='guest')[0]
            obj.user.groups.add(group)
            obj.status = status
            obj.save()
            return HttpResponseRedirect('/bids/bidsdouble')
        else:
            if bids_form.is_valid():
                try:
                    obj = bids_form.save(commit=False)
                    obj.user = prof.user
                    group = Group.objects.get_or_create(name='guest')[0]
                    obj.user.groups.add(group)
                    obj.status = status
                    obj.save()
                    return HttpResponseRedirect('/bids/bids')
                except Exception as err:
                    print(err)
            else:
                messages.error(request, 'Please correct the error below.')
    else:
        bids_user_form = UserAdd()
        bids_form = BidsAdd()
    return render(request, 'bids/bids_add.html',
                  {'bids_form': bids_form,
                   'bids_user_form': bids_user_form,
                    "f_status": f_status})


class StatusHistoryView(ListView):
    template_name = 'bids/status_history.html'
    model = StatusHistory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        edit_id = self.request.GET.get('edit_id', None)
        context["edit_id"] = edit_id
        context["history_list"] = StatusHistory.objects.filter(bid=Bid.objects.get(pk=edit_id)).order_by(
            "-created_date")
        return context

    def get_queryset(self, **kwargs):
        return StatusHistory.objects.all()


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
                        # obj = BidDouble.objects.create(**dict_str)
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
