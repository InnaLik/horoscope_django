from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from django.urls import reverse

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


def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope_name', args=(sign,))
        li_elements += f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    response = f"""
                <ul>
                    {li_elements}
                </ul>"""
    return HttpResponse(response)


def type_horoscope(request):
    type_list = ['Fire', 'Earth', 'Air', 'Water']
    li_elements = ''
    for j in type_list:
        redirect_path = reverse('nature', args=(j,))
        li_elements += f"<li> <a href='{redirect_path}'>{j} </a> </li>"
    response = f"""
                    <ul>
                        {li_elements}
                    </ul>"""
    return HttpResponse(response)


nature_dict = {'Fire': ['aries', 'leo', 'sagittarius'], 'Earth': ['taurus', 'virgo', 'capricorn'],
               'Air': ['gemini', 'libra', 'aquarius'],
               'Water': ['cancer', 'scorpio', 'pisces']}


def nature(request, type_nature):
    li_elements = {}
    for i, j in nature_dict.items():
        li = ''
        for k in j:
            redirect_path = reverse('horoscope_name', args=(k, ))
            li += f'<li> <a href="{redirect_path}"> {k} </a> </li>'
        #тут будет словарь ключом будет являться стихия, а значением html шаблон со ссылками на знаки зодиака
        li_elements[i] = li
    #соответственно тут подставляя тип стихии, я беру наш html шаблон и уже его передаю в ответ
    answer = li_elements[type_nature]
    return HttpResponse(answer)


def get_info_by_date(request, month, day):
    return HttpResponse




def get_info_about_sign_zodiac(request, sign_zodiac: str):
    answer = zodiac_dict.get(sign_zodiac)
    if answer:
        return HttpResponse(answer)
    return HttpResponse(f'Неизвестный знак зодиака - {sign_zodiac}')


def get_info_about_by_number(request, int_zodiac: int):
    zodiac = list(zodiac_dict)
    if int_zodiac > len(zodiac):
        return HttpResponseNotFound(f'Неправильный порядковый номер {int_zodiac}')
    name_zodiac = zodiac[int_zodiac - 1]
    uri = reverse('horoscope_name', args=(name_zodiac,))
    return redirect(uri)
