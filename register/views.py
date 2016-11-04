from django.shortcuts import reverse
from django.contrib.auth import get_user_model, login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, RedirectView

from registration.backends.default.views import RegistrationView

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
