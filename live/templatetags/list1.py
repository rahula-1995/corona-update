from django import template

register = template.Library()

@register.filter
def list1(value,args):
    return value[args]