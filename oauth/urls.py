from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^applications/$', views.ApplicationList.as_view(), name='list'),
    url(r'^', include('oauth2_provider.urls')),
]
