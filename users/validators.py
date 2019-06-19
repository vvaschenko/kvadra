# coding=utf-8
import regex

from django.core.exceptions import ValidationError


def validate_birthday(value):
    delimetrs = ['.', '-']

    if delimetrs[0] in value or delimetrs[1] in value:

        for delimetr in delimetrs:

            if delimetr in value:
                day, month, year = value.split(delimetr)

                if len(day) == 2 and len(month) == 2 and len(year) == 4:
                    pass
                else:
                    raise ValidationError(
                        message="Дата рождения должна быть в одном из форматов: дд.мм.гггг или дд-мм-гггг"
                    )
    else:
        raise ValidationError(
            message="Дата рождения должна быть в одном из форматов: дд.мм.гггг или дд-мм-гггг"
        )


def validate_contact_phone_numeric(value):
    if not value.isnumeric():
        raise ValidationError(
            message="Номер телефона должен быть в формате 380991115599"
        )


def validate_contact_phone_length(value):
    if len(value) != 12:
        raise ValidationError(
            message="Длина номера должна равняться 12"
        )


def validate_passport_series(value):
    splitted = list(value)
    is_cyrillic = []
    for s in splitted:
        is_cyrillic.append(
            True if regex.search(r'\p{IsCyrillic}', s) else False
        )

    if not all(is_cyrillic) or splitted is None or splitted == "":
        raise ValidationError(
            message="Серия паспорта должна состоять полностью из символов Кириллицы"
        )
