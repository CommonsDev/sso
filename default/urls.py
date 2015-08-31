from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='registration_register'),
    url(r'^$', views.HomeView.as_view(), name='auth_login'),
    url(r'^$', views.HomeView.as_view(), name='homepage'),
)
