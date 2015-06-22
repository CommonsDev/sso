from oauth2_provider.views.application import (
    ApplicationUpdate as BaseApplicationUpdate)
from oauth2_provider.views.application import (
    ApplicationRegistration as BaseApplicationRegistration)

from .forms import RegistrationForm

class ApplicationUpdate(BaseApplicationUpdate):
    """
    View used to register a new Application for the request.user.
    Overriding oauth2_provider.views.application.ApplicationUpdate to remove
    the `user_id` field.
    """
    fields = ('name', 'client_type', 'authorization_grant_type', 'client_id',
              'client_secret', 'redirect_uris', 'skip_authorization')
