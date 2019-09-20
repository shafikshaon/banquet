from django import template

register = template.Library()


@register.filter(name='sentence_case')
def sentence_case(value):
    item_list = value.split(':')
    item_length = len(item_list)
    column = {}
    if item_length == 1:
        value = item_list[0].replace('_', ' ')
        column.update({'name': value})
        value = value.capitalize()
        column.update({'display_name': value})
        column.update({'type': 'text'})
        return column
    if item_length == 2:
        column.update({'name': item_list[0]})
        value = item_list[1].replace('_', ' ')
        column.update({'display_name': value})
        column.update({'type': 'text'})
        return column
    if item_length == 3:
        column.update({'name': item_list[0]})
        value = item_list[1].replace('_', ' ')
        column.update({'display_name': value})
        column.update({'type': item_list[2]})
        return column
