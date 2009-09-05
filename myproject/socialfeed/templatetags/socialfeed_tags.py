from django import template

register = template.Library()
from myproject.socialfeed.models import Link

def socialfeed(context):
    return {
        'links': Link.objects.all(),
        'sponsors': context['sponsors'],
        'current_user': context['current_user'],
    }
# Register the custom tag as an inclusion tag with takes_context=True.
register.inclusion_tag('socialfeed/_box.html', takes_context=True)(socialfeed)