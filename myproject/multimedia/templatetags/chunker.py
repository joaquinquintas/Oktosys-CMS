from django import template

from itertools import izip_longest

register = template.Library()

@register.filter(name='chunk')
def chunk(iterable, n):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=None)
