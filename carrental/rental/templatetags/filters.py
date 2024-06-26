from django import template

register = template.Library()

@register.filter(name='replace_comma_with_dot')
def replace_comma_with_dot(value):
    return str(value).replace(',', '.')
