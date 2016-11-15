from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from oauth2_provider.views import ScopedProtectedResourceView

from core.decorators import class_decorator


@class_decorator(login_required)
class ProfileView(ScopedProtectedResourceView):
    required_scopes = ['read']

    def get(self, request, *args, **kwargs):
        user = request.user
        return JsonResponse({
            'id': user.pk,
            'email': user.email,
        })
