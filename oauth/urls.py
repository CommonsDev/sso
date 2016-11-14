from django.conf.urls import include, url
from django.contrib.admin.views.decorators import staff_member_required

from oauth2_provider import views


urlpatterns = [
    url(r'^applications/', staff_member_required()(
        views.ApplicationList.as_view()), name='list'),
    url(r'^applications/register/', staff_member_required()(
        views.ApplicationRegistration.as_view()), name='register'),
    url(r'', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
