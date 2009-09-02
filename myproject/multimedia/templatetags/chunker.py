from django import template

register = template.Library()

@register.filter(name='chunk')
def chunk(iterable, n):
    return izip(*[chain(iterable, repeat(None, n - 1))] * n)
