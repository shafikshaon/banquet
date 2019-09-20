from django import template

register = template.Library()


@register.filter(name='normalize')
def normalize(value):
    if value:
        return value
    else:
        return 'N/A'
