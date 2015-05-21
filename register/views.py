from registration.backends.default.views import ActivationView
from registration.backends.default.views import RegistrationView

from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = 'register/profile.html'
