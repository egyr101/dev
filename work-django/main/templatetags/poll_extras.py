from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()
@register.simple_tag()
def linkk(categories=None, name = None):
    return f'http://127.0.0.1:8000/{categories}/{name}'