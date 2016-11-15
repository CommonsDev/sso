from django.contrib.auth import authenticate
from django.http import HttpResponse


class OAuth2TokenMiddleware:
    """
    Django 1.10 has changed the middlewares signature.
    oauth2_provider.middleware.OAuth2TokenMiddleware is still old style.
    https://github.com/evonove/django-oauth-toolkit/issues/406
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META.get('HTTP_AUTHORIZATION', '').startswith('Bearer'):
            if not hasattr(request, 'user') or request.user.is_anonymous():
                user = authenticate(request=request)
                if user:
                    request.user = request._cached_user = user
                else:
                    response = HttpResponse('Unauthorized', status=401)
                    response['WWW-Authenticate'] = (
                        'Bearer realm="api"')
                    return response

        return self.get_response(request)
