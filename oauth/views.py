from oauth2_provider.views.application import (
    ApplicationUpdate as BaseApplicationUpdate)
from oauth2_provider.forms import RegistrationForm


class ApplicationUpdate(BaseApplicationUpdate):
    """
    View used to register a new Application for the request.user.
    Overriding oauth2_provider.views.application.ApplicationUpdate to remove
    the `user_id` field.
    """
    fields = RegistrationForm._meta.fields
