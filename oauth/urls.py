"""
This file was copy/past-ed from oauth2_provider.urls due to the need of
overriding the 'update' url.
A better way should be found here not to have the entire url conf file
duplicated.
"""
from __future__ import absolute_import

from django.conf.urls import patterns, url

from oauth2_provider import views as base_views

from . import views


urlpatterns = patterns(
    '',
    url(r'^authorize/$', base_views.AuthorizationView.as_view(), name="authorize"),
    url(r'^token/$', base_views.TokenView.as_view(), name="token"),
    url(r'^revoke_token/$', base_views.RevokeTokenView.as_view(), name="revoke-token"),
)

# Application management oauth2_provider views
urlpatterns += patterns(
    '',
    url(r'^applications/$', base_views.ApplicationList.as_view(), name="list"),
    url(r'^applications/register/$', base_views.ApplicationRegistration.as_view(), name="register"),
    url(r'^applications/(?P<pk>\d+)/$', base_views.ApplicationDetail.as_view(), name="detail"),
    url(r'^applications/(?P<pk>\d+)/delete/$', base_views.ApplicationDelete.as_view(), name="delete"),
    url(r'^applications/(?P<pk>\d+)/update/$', views.ApplicationUpdate.as_view(), name="update"),
)
