from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='split_f')
@stringfilter
def split_f(value, key=' '):
    return value.split(key)

@register.filter(name='first_v')
def first_v(value):
    return value[0]
