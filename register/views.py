from django.views.generic import TemplateView, RedirectView
from django.shortcuts import reverse

from registration.backends.default.views import RegistrationView  # noqa


class ProfileView(TemplateView):
    template_name = 'register/profile.html'


class NextRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        try:
            redirect = self.request.session.pop('next')
        except KeyError:
            return reverse('homepage')
        return redirect
