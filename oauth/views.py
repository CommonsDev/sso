from oauth2_provider.views.application import (
    ApplicationList as BaseApplicationList
)


class ApplicationList(BaseApplicationList):
    template_name = 'registration/profile.html'
