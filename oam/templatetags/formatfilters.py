from django import template
import locale

try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

register = template.Library()


@register.filter()
def currency(value):
    return locale.currency(value, grouping=True)
