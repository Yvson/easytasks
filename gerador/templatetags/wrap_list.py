from django import template

register = template.Library()


@register.filter(name='wraplist')
def wraplist(value, columns):
    initial_list = value.replace(' ', '')
    initial_list = initial_list.split(',')
    numbers_list = []

    for n, i in enumerate(initial_list):
        if (n % int(columns) == 0):
            numbers_list.append(initial_list[n:n+int(columns)])

    return numbers_list
