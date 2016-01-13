from django import template
import locale

try:
  locale.setlocale(locale.LC_ALL, 'en_US.utf8')
except:
  pass

register = template.Library()


@register.filter()
def currency(value):
    return locale.currency(value, grouping=True)
