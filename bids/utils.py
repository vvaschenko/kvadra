# coding=utf-8
import json

import requests
import MySQLdb
import xlrd

from django.conf import settings

# from bids.models import ResufedBid

# 
# def send_to_salesdoubler(bid_object):
#     endpoint = "http://api.admin.salesdoubler.net/leads/sgroshi/"
# 
#     data_for_sending = {
#         "name": " ".join([
#             bid_object.last_name,
#             bid_object.first_name,
#             bid_object.middle_name,
#         ]),
#         "mobile_phone": bid_object.contact_phone[2:],
#         "affice_code": "63893"
#     }
# 
#     request_headers = {
#         "Content-Type": "application/json",
#         "Access-Token": "ea338ba42fb50bf2fe83783b9e4dc174"
#     }
# 
#     r = requests.post(
#         endpoint,
#         data=json.dumps(data_for_sending),
#         headers=request_headers
#     )
# 
#     """
#     Example response:
#     {
#         "status":"ok",
#         "message":{
#             "Was Added Record #1245:":{
#                 "affice_code":"63893",
#                 "name":"  ",
#                 "mobile_phone":"0661223992",
#                 "campaign":"",
#                 "source":"",
#                 "promo":"",
#                 "custom_param1":"",
#                 "custom_param2":"",
#                 "platform":"shvydko_groshi",
#                 "status":"2",
#                 "cdate":"2018-05-02 09:27:28"
#             }
#         }
#     }
#     """
# 
#     try:
#         if r.json()["status"] == "ok":
#             ResufedBid.objects.create(
#                 provider="Salesdoubler",
#                 response_text=r.text,
#                 success_sent=True,
#                 bid=bid_object
#             )
#         else:
#             ResufedBid.objects.create(
#                 provider="Salesdoubler",
#                 response_text=r.text,
#                 success_sent=False,
#                 bid=bid_object
#             )
#     except Exception as e:
#         print(e)
#         ResufedBid.objects.create(
#             provider="Salesdoubler",
#             response_text=r.text,
#             success_sent=False,
#             bid=bid_object
#         )
# 
#     return r.text

# 
# def send_to_finline(bid_object):
#     endpoint = "http://partner.finline.ua/api/apply/"
# 
#     data_for_sending = {
#         "phone": "+" + bid_object.contact_phone,
#         "city": bid_object.city or 'Kyiv',
#         "offerCode": "cashCard",
#         "employment": "no",
#         "partner": 3897
#     }
#     if bid_object.birthday:
#         data_for_sending["birthDate"] = bid_object.birthday.replace('-', '.')
# 
#     if bid_object.first_name:
#         data_for_sending["firstName"] = bid_object.first_name
# 
#     if bid_object.last_name:
#         data_for_sending["lastName"] = bid_object.last_name
# 
#     if bid_object.itn:
#         data_for_sending["identCode"] = bid_object.itn
# 
#     r = requests.get(
#         endpoint,
#         params=data_for_sending
#     )
# 
#     # print(r.text)
#     try:
#         if r.json()["result"]:
#             ResufedBid.objects.create(
#                 provider="Finline",
#                 response_text=r.text,
#                 success_sent=True,
#                 bid=bid_object
#             )
#         else:
#             ResufedBid.objects.create(
#                 provider="Finline",
#                 response_text=r.text,
#                 success_sent=False,
#                 bid=bid_object
#             )
#     except Exception as e:
#         print(e)
#         ResufedBid.objects.create(
#             provider="Finline",
#             response_text=r.text,
#             success_sent=False,
#             bid=bid_object
#         )
# 

def send_to_vici(bid_object):
    # sending to Kiev Contact center
    try:
        db = MySQLdb.connect(host=settings.VICI_KYIV_HOST,
                             user=settings.VICI_KYIV_USER,
                             passwd=settings.VICI_KYIV_PASSWORD,
                             db=settings.VICI_KYIV_DATABASE,
                             port=9906,
                             use_unicode=True)
        db.set_character_set('utf8')
        cur = db.cursor()
        cur.execute('SET NAMES utf8;')
        cur.execute('SET CHARACTER SET utf8;')
        cur.execute('SET character_set_connection=utf8;')

        cur.execute(
            """INSERT INTO
               komfina (idcrm, lastname, firstname, city, phone, email, suma, future)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""",
            (
                bid_object.id,
                bid_object.last_name or 'empty',
                bid_object.first_name or 'empty',
                bid_object.city,
                bid_object.contact_phone,
                bid_object.email or 'empty',
                bid_object.credit_sum or 0,
                bid_object.itn if bid_object.itn else 'empty INN'
            )
        )
        db.commit()  # without this, do not save insert
        db.close()
        return True
    except Exception:
        return False


def send_to_vici2(bid_object):
    # sending to Kirovograd Contact center
    try:
        db = MySQLdb.connect(host=settings.VICI_KIROV_HOST,
                             user=settings.VICI_KIROV_USER,
                             passwd=settings.VICI_KIROV_PASSWORD,
                             db=settings.VICI_KIROV_DATABASE,
                             port=9906,
                             use_unicode=True)
        db.set_character_set('utf8')
        cur = db.cursor()
        cur.execute('SET NAMES utf8;')
        cur.execute('SET CHARACTER SET utf8;')
        cur.execute('SET character_set_connection=utf8;')

        cur.execute(
            """INSERT INTO
               komfina (idcrm, lastname, firstname, city, phone, email, suma, future)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""",
            (
                bid_object.id,
                bid_object.last_name or 'empty',
                bid_object.first_name or 'empty',
                bid_object.city,
                bid_object.contact_phone,
                bid_object.email or 'empty',
                bid_object.credit_sum or 0,
                bid_object.itn if bid_object.itn else 'empty INN'
            )
        )
        db.commit()  # without this, do not save insert
        db.close()
        return True
    except Exception:
        return False


def group_send_to_vici(bid_object, cursor, db):
    # sending to Kiev Contact center
    try:
        cursor.execute(
            """INSERT INTO
               komfina (idcrm, lastname, firstname, city, phone, email, suma, future)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""",
            (
                bid_object.id,
                bid_object.last_name or 'empty',
                bid_object.first_name or 'empty',
                bid_object.city,
                bid_object.contact_phone,
                bid_object.email or 'empty',
                bid_object.credit_sum or 0,
                bid_object.itn if bid_object.itn else 'empty INN'
            )
        )
        db.commit()  # without this, do not save insert
        return True
    except Exception:
        return False


def group_send_to_vici2(bid_object, cursor, db):
    # sending to Kirovograd Contact center w/o filter by partner
    try:
        cursor.execute(
            """INSERT INTO
               komfina (idcrm, lastname, firstname, city, phone, email, suma, future)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s);""",
            (
                bid_object.id,
                bid_object.last_name or 'empty',
                bid_object.first_name or 'empty',
                bid_object.city,
                bid_object.contact_phone,
                bid_object.email or 'empty',
                bid_object.credit_sum or 0,
                bid_object.itn if bid_object.itn else 'empty INN'
            )
        )
        db.commit()  # without this, do not save insert
        return True
    except Exception:
        return False



def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def get_value(d, key):
    prom_value = d.get(key)
    if prom_value is None:
        prom_value = ""
    return prom_value


def get_value_excel(book, sheet, row, col):
    type_cell = sheet.cell(row, col).ctype
    """
    1 - "текстовый" выводим как есть.
    2 - "числовой"  округляем и приводим к строке.
    3 - "Дата"  Преобразуем дату в текст.
    """
    if type_cell == 0:
        cell_value = sheet.cell(row, col).value
    if type_cell == 1:
        cell_value = sheet.cell(row, col).value
    if type_cell == 2:
        cell_value = str(int(sheet.cell(row, col).value))
    if type_cell == 3:
        try:
            cell_value = xlrd.xldate.xldate_as_datetime(sheet.cell(row, col).value, book.datemode)
        except xlrd.xldate.XLDateError as err:
            print(err)
            # cell_value = ""
    return cell_value


def list_name_tuple():
    listname = {
        'partner_name': ('Партнер', 'partner_name'),
        'lead_id': ('ID клиента', 'lead_id'),
        'webmaster_id': ('Webmaster ID', 'webmaster_id'),
        'credit_sum': ('Сумма кредита', 'credit_sum'),
        'first_name': ('Имя', 'first_name'),
        'middle_name': ('Отчество', 'middle_name'),
        'last_name': ('Фамилия', 'last_name'),
        'birthday': ('Дата рождения', 'birthday'),
        'itn': ('ИНН', 'itn'),
        'email': ('Email', 'email'),
        'contact_phone': ('Номер телефона', 'contact_phone'),
        'number_phone1': ('Номер телефона 1', 'number_phone1'),
        'cod_number_phone1': ('Код телефона 1', 'cod_number_phone1'),
        'number_phone2': ('Номер телефона 2', 'number_phone2'),
        'cod_number_phone2': ('Код телефона 2', 'cod_number_phone2'),
        'number_phone3': ('Номер телефона 3', 'number_phone3'),
        'cod_number_phone3': ('Код телефона 3', 'cod_number_phone3'),
        'number_phone4': ('Номер телефона 4', 'number_phone4'),
        'cod_number_phone4': ('Код телефона 4', 'cod_number_phone4'),
        'number_phone5': ('Номер телефона 5', 'number_phone5'),
        'cod_number_phone5': ('Код телефона 5', 'cod_number_phone5'),
        'number_Viber': ('Номер Viber', 'number_Viber'),
        'number_WhatsApp': ('Номер WhatsApp', 'number_WhatsApp'),
        'number_Telegram': ('Номер Telegram', 'number_Telegram'),
        'status_Viber': ('Статус Viber', 'status_Viber'),
        'place_of_work': ('Місце Роботи', 'place_of_work'),
        'position': ('Посада', 'position'),
        'number_phone_work': ('Номер телефона рабочий', 'number_phone_work'),
        'cod_number_phone_work': ('Код телефона рабочий', 'cod_number_phone_work'),
        'income': ('Дохід', 'income'),
        'other_income': ('Інший Дохід', 'other_income'),
        'family_income': ('Сімейний Дохід', 'family_income'),
        'total_income': ('Загальний Дохід', 'total_income'),
        'registration_area_ur': ('Область Реєстрації', 'registration_area_ur'),
        'registration_raion_ur': ('Район Реєстрації', 'registration_raion_ur'),
        'registration_city_ur': ('Місто Реєстрації', 'registration_city_ur'),
        'registration_street_ur': ('Вулиця Реєстрації', 'registration_street_ur'),
        'House_number_ur': ('Номер Будинку Реєстрації', 'House_number_ur'),
        'apartment_number_ur': ('Номер Квартири Реєстрації', 'apartment_number_ur'),
        'registration_area_fiz': ('Область Проживання', 'registration_area_fiz'),
        'registration_raion_fiz': ('Район Проживання', 'registration_raion_fiz'),
        'registration_city_fiz': ('Місто Проживання', 'registration_city_fiz'),
        'registration_street_fiz': ('Вулиця Проживання', 'registration_street_fiz'),
        'House_number_fiz': ('Номер Будинку Проживання', 'House_number_fiz'),
        'apartment_number_fiz': ('Номер Квартири Проживання', 'apartment_number_fiz'),
        'passport_series': ('Серия паспорта', 'passport_series'),
        'passport_number': ('Номер паспорта', 'passport_number'),
        'issued_by': ('Паспорт Ким Видано', 'issued_by'),
        'date_of_issue': ('Паспорт Дата Видачі', 'date_of_issue'),
        'name_base': ('Назва Бази', 'name_base'),
        'mailing_list': ('Участь в розсилках', 'mailing_list'),
        'remark': ('Примітка', 'remark'),
        'base_id': ('ID бази', 'base_id'),
        'name_project': ('Назва проекту', 'name_project'),
        'project_id': ('ID проекту', 'project_id'),
        'city': ('Город', 'city'),
        # 'status': ('Статус заявки', 'status'),
        'crm_status': ('CRM status', 'crm_status'),
        'created_dt': ('Дата создания', 'created_dt'),
        'updated_dt': ('Дата изменения', 'updated_dt'),
        'site_bid_id': ('ID заявки на сайте kvadraonline', 'site_bid_id')
        # 'for_skybank': ('Передано на Skybank', 'for_skybank')
    }
    return listname

#
# def for_save(obj, batchlist):
#     if batchlist.get('partner_name') is None:
#         pass
#     else:
#         obj.partner_name = batchlist['partner_name']
#     if batchlist.get('lead_id') is None:
#         pass
#     else:
#         obj.lead_id = batchlist['lead_id']
#     if batchlist.get('webmaster_id') is None:
#         pass
#     else:
#         obj.webmaster_id = batchlist['webmaster_id']
#     if batchlist.get('credit_sum') is None:
#         pass
#     else:
#         obj.credit_sum = batchlist['credit_sum']
#     if batchlist.get('first_name') is None:
#         pass
#     else:
#         obj.first_name = batchlist['first_name']
#     if batchlist.get('middle_name') is None:
#         pass
#     else:
#         obj.middle_name = batchlist['middle_name']
#     if batchlist.get('last_name') is None:
#         pass
#     else:
#         obj.last_name = batchlist['last_name']
#     if batchlist.get('birthday') is None:
#         pass
#     else:
#         obj.birthday = batchlist['birthday']
#     if batchlist.get('itn') is None:
#         pass
#     else:
#         obj.itn = batchlist['itn']
#     if batchlist.get('email') is None:
#         pass
#     else:
#         obj.email = batchlist['email']
#     if batchlist.get('contact_phone') is None:
#         pass
#     else:
#         obj.contact_phone = batchlist['contact_phone']
#     if batchlist.get('number_phone1') is None:
#         pass
#     else:
#         obj.number_phone1 = batchlist['number_phone1']
#     if batchlist.get('cod_number_phone1') is None:
#         pass
#     else:
#         obj.cod_number_phone1 = batchlist['cod_number_phone1']
#     if batchlist.get('number_phone2') is None:
#         pass
#     else:
#         obj.number_phone2 = batchlist['number_phone2']
#     if batchlist.get('cod_number_phone2') is None:
#         pass
#     else:
#         obj.cod_number_phone2 = batchlist['cod_number_phone2']
#     if batchlist.get('number_phone3') is None:
#         pass
#     else:
#         obj.number_phone3 = batchlist['number_phone3']
#     if batchlist.get('cod_number_phone3') is None:
#         pass
#     else:
#         obj.cod_number_phone3 = batchlist['cod_number_phone3']
#     if batchlist.get('number_phone4') is None:
#         pass
#     else:
#         obj.number_phone4 = batchlist['number_phone4']
#     if batchlist.get('cod_number_phone4') is None:
#         pass
#     else:
#         obj.cod_number_phone4 = batchlist['cod_number_phone4']
#     if batchlist.get('number_phone5') is None:
#         pass
#     else:
#         obj.number_phone5 = batchlist['number_phone5']
#     if batchlist.get('cod_number_phone5') is None:
#         pass
#     else:
#         obj.cod_number_phone5 = batchlist['cod_number_phone5']
#     if batchlist.get('number_Viber') is None:
#         pass
#     else:
#         obj.number_Viber = batchlist['number_Viber']
#     if batchlist.get('number_WhatsApp') is None:
#         pass
#     else:
#         obj.number_WhatsApp = batchlist['number_WhatsApp']
#     if batchlist.get('number_Telegram') is None:
#         pass
#     else:
#         obj.number_Telegram = batchlist['number_Telegram']
#     if batchlist.get('status_Viber') is None:
#         pass
#     else:
#         obj.status_Viber = batchlist['status_Viber']
#     if batchlist.get('place_of_work') is None:
#         pass
#     else:
#         obj.place_of_work = batchlist['place_of_work']
#     if batchlist.get('position') is None:
#         pass
#     else:
#         obj.position = batchlist['position']
#     if batchlist.get('number_phone_work') is None:
#         pass
#     else:
#         obj.number_phone_work = batchlist['number_phone_work']
#     if batchlist.get('cod_number_phone_work') is None:
#         pass
#     else:
#         obj.cod_number_phone_work = batchlist['cod_number_phone_work']
#     if batchlist.get('income') is None:
#         pass
#     else:
#         obj.income = batchlist['income']
#     if batchlist.get('other_income') is None:
#         pass
#     else:
#         obj.other_income = batchlist['other_income']
#     if batchlist.get('family_income') is None:
#         pass
#     else:
#         obj.family_income = batchlist['family_income']
#     if batchlist.get('total_income') is None:
#         pass
#     else:
#         obj.total_income = batchlist['total_income']
#     if batchlist.get('registration_area_ur') is None:
#         pass
#     else:
#         obj.registration_area_ur = batchlist['registration_area_ur']
#     if batchlist.get('registration_raion_ur') is None:
#         pass
#     else:
#         obj.registration_raion_ur = batchlist['registration_raion_ur']
#     if batchlist.get('registration_city_ur') is None:
#         pass
#     else:
#         obj.registration_city_ur = batchlist['registration_city_ur']
#     if batchlist.get('registration_street_ur') is None:
#         pass
#     else:
#         obj.registration_street_ur = batchlist['registration_street_ur']
#     if batchlist.get('House_number_ur') is None:
#         pass
#     else:
#         obj.House_number_ur = batchlist['House_number_ur']
#     if batchlist.get('apartment_number_ur') is None:
#         pass
#     else:
#         obj.apartment_number_ur = batchlist['apartment_number_ur']
#     if batchlist.get('registration_area_fiz') is None:
#         pass
#     else:
#         obj.registration_area_fiz = batchlist['registration_area_fiz']
#     if batchlist.get('registration_raion_fiz') is None:
#         pass
#     else:
#         obj.registration_raion_fiz = batchlist['registration_raion_fiz']
#     if batchlist.get('registration_city_fiz') is None:
#         pass
#     else:
#         obj.registration_city_fiz = batchlist['registration_city_fiz']
#     if batchlist.get('registration_street_fiz') is None:
#         pass
#     else:
#         obj.registration_street_fiz = batchlist['registration_street_fiz']
#     if batchlist.get('House_number_fiz') is None:
#         pass
#     else:
#         obj.House_number_fiz = batchlist['House_number_fiz']
#     if batchlist.get('apartment_number_fiz') is None:
#         pass
#     else:
#         obj.apartment_number_fiz = batchlist['apartment_number_fiz']
#     if batchlist.get('passport_series') is None:
#         pass
#     else:
#         obj.passport_series = batchlist['passport_series']
#     if batchlist.get('passport_number') is None:
#         pass
#     else:
#         obj.passport_number = batchlist['passport_number']
#     if batchlist.get('issued_by') is None:
#         pass
#     else:
#         obj.issued_by = batchlist['issued_by']
#     if batchlist.get('date_of_issue') is None:
#         pass
#     else:
#         obj.date_of_issue = batchlist['date_of_issue']
#     if batchlist.get('name_base') is None:
#         pass
#     else:
#         obj.name_base = batchlist['name_base']
#     if batchlist.get('mailing_list') is None:
#         pass
#     else:
#         obj.mailing_list = batchlist['mailing_list']
#     if batchlist.get('remark') is None:
#         pass
#     else:
#         obj.remark = batchlist['remark']
#     if batchlist.get('base_id') is None:
#         pass
#     else:
#         obj.base_id = batchlist['base_id']
#     if batchlist.get('name_project') is None:
#         pass
#     else:
#         obj.name_project = batchlist['name_project']
#     if batchlist.get('project_id') is None:
#         pass
#     else:
#         obj.project_id = batchlist['project_id']
#     if batchlist.get('city') is None:
#         pass
#     else:
#         obj.city = batchlist['city']
#     if batchlist.get('status') is None:
#         pass
#     else:
#         obj.status = batchlist['status']
#     if batchlist.get('crm_status') is None:
#         pass
#     else:
#         obj.crm_status = batchlist['crm_status']
#     if batchlist.get('created_dt') is None:
#         pass
#     else:
#         obj.created_dt = batchlist['created_dt']
#     if batchlist.get('updated_dt') is None:
#         pass
#     else:
#         obj.updated_dt = batchlist['updated_dt']
#     if batchlist.get('site_bid_id') is None:
#         pass
#     else:
#         obj.site_bid_id = batchlist['site_bid_id']
#
#     return obj
