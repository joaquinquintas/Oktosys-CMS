from django import template

register = template.Library()

def socialfeed(context):
    return {
        'sponsors': context['sponsors'],
        'current_user': context['current_user'],
    }
# Register the custom tag as an inclusion tag with takes_context=True.
register.inclusion_tag('socialfeed/_box.html', takes_context=True)(socialfeed)