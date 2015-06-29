from django.template import Library
from django.core.urlresolvers import reverse

register = Library()

@register.simple_tag(takes_context=True)
def absurl(context, *args, **kwargs):
    request = context.request
    absolute = 'http{ssl}://{domain}{url}'.format(
        ssl=('s' if request.is_secure() else ''),
        domain=request.META['HTTP_HOST'],
        url=reverse(*args, **kwargs)
    )
    return absolute
