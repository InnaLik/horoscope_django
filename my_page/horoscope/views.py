from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
import datetime

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

zodiac_month = {'aries': [80, 110],
                'taurus': [111, 141],
                'gemini': [142, 172],
                'cancer': [173, 203],
                'leo': [204, 233],
                'virgo': [234, 266],
                'libra': [267, 296],
                'scorpio': [297, 326],
                'sagittarius': [327, 356],
                'capricorn': [357, 20],
                'aquarius': [21, 50],
                'pisces': [51, 79]}

zodiac_type = {'Fire': ['aries', 'leo', 'sagittarius'],
               'Earth': ['taurus', 'virgo', 'capricorn'],
               'Air': ['gemini', 'libra', 'aquarius'],
               'Water': ['cancer', 'scorpio', 'pisces']}


def main_type(request):
    d = {'title': list(zodiac_type)}
    return render(request, 'horoscope/horoscope_type.html', d)


def horoscope_month(request, month, day):
    d_z = ''
    d = datetime.date(year=2023, month=month, day=day)
    try:
        d = datetime.date(year=2023, month=month, day=day)
        e = d.toordinal() - 738520
        if 20 < e < 357:
            for i in zodiac_month:
                if zodiac_month[i][0] <= e <= zodiac_month[i][1]:
                    d_z = i
                    break
        else:
            d_z = 'capricorn'
        return HttpResponse(zodiac_dict[d_z])
    except:
        return HttpResponseNotFound('Неверный номер дня или месяца')


def type_zodiac(request, element):
    list_element = zodiac_type[element]
    d = {'title': element,
         'values_z': list_element}
    return render(request, 'horoscope/element_zodiac.html', d)


def zod(request, zodiak: str):
    d = {'title': zodiak,
         'info': zodiac_dict[zodiak]}
    return render(request, 'horoscope/info.html', d)


def main_menu(request):
    d = {'title': list(zodiac_dict)}
    return render(request, 'horoscope/main_page.html', d)


def by_number(request, zodiak: int):
    z = list(zodiac_dict.keys())
    if 1 <= zodiak <= 12:
        uri = reverse('horoscope_name', args=(z[zodiak - 1],))
        return redirect(uri, permanent=True)
    return HttpResponseNotFound(f'Был передан неправильный порядковый номер {zodiak}')


def get_converters(request, zodiak):
    return HttpResponse(f'{zodiak}')


def float_converters(request, zodiak):
    return HttpResponse(f'float {zodiak}')


def people(request):
    peoples = [
        {'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
        {'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
        {'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
        {'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
        {'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
        {'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
        {'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
        {'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
        {'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
        {'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
    ]
    return render(request, 'horoscope/people.html', {'peoples': peoples})
