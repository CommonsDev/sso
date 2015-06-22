from oauth2_provider.forms import RegistrationForm as BaseRegistrationForm


class RegistrationForm(BaseRegistrationForm):
    class Meta:
        fields = ('client_id',)
