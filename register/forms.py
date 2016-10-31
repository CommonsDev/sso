from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.fields import EmailField
from registration.forms import RegistrationForm

from default.widgets import Display


class EmailPrefilledMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'email' in self.fields:
            self.fields['email'].widget = Display()


class EmailForm(forms.Form):
    email = forms.EmailField(required=True)


class LoginForm(EmailPrefilledMixin, AuthenticationForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        email = kwargs['initial'].get('email')
        kwargs['initial']['username'] = email
        if 'data' in kwargs:
            kwargs['data'] = dict(kwargs['data'])
            kwargs['data']['username'] = email
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = Display()


class RegisterForm(EmailPrefilledMixin, RegistrationForm):
    def __init__(self, *args, **kwargs):
        if 'data' in kwargs and 'password1' in kwargs['data']:
            kwargs['data'] = dict(kwargs['data'])
            kwargs['data']['password2'] = kwargs['data']['password1']
        super().__init__(*args, **kwargs)
        self.fields['password2'].required = False
        self.fields['password2'].widget.input_type = 'hidden'
