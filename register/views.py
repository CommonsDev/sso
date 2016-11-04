from django.shortcuts import reverse
from django.contrib.auth import get_user_model, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, RedirectView

from registration import signals
from registration.backends.default.views import RegistrationView
from registration.models import RegistrationProfile
from registration.users import UserModel

from . import forms


class ProfileView(TemplateView):
    template_name = 'register/profile.html'


class EmailView(FormView):
    template_name = 'registration/email.html'
    success_url_login = reverse_lazy('auth_login')
    success_url_register = reverse_lazy('auth_register')
    form_class = forms.EmailForm

    def form_valid(self, form):
        self.request.session['email'] = form.data.get('email')
        return super().form_valid(form)

    def get_success_url(self):
        email = self.request.session['email']
        User = get_user_model()
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return self.success_url_register
        return self.success_url_login


class EmailPrefilledMixin:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        email = self.request.session.get('email')
        kwargs['initial']['email'] = email
        if 'data' in kwargs:
            kwargs['data'] = dict(self.request.POST)
            kwargs['data']['email'] = email
        return kwargs


class LoginView(EmailPrefilledMixin, FormView):
    template_name = 'registration/login.html'
    form_class = forms.LoginForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.session.get('next') or reverse('homepage')


class RegisterView(EmailPrefilledMixin, RegistrationView):
    template_name = 'registration/register.html'
    form_class = forms.RegisterForm

    def register(self, form):
        """
        We need to inject `next` into the template.
        Hackish way is to use `site` that is passed through the template.
        """
        site = get_current_site(self.request)
        # Hackish here injecting the `next` to a template accessed variable.
        site.next = self.request.session.get('next')

        if hasattr(form, 'save'):
            new_user_instance = form.save()
        else:
            new_user_instance = (UserModel().objects
                                 .create_user(**form.cleaned_data))
        new_user = RegistrationProfile.objects.create_inactive_user(
            new_user=new_user_instance,
            site=site,
            send_email=self.SEND_ACTIVATION_EMAIL,
            request=self.request,
        )
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        return new_user


class LogoutView(RedirectView):
    url = reverse_lazy('homepage')

    def get(self, request, *args, **kwargs):
        logout(self.request)
        return super().get(request, *args, **kwargs)


class NextRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        try:
            redirect = self.request.session.pop('next')
        except KeyError:
            return reverse('homepage')
        return redirect
