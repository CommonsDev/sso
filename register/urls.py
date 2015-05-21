from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('',
    url(r'^register/profile/$', views.ProfileView.as_view(),
        name='register_profile'),
    url(r'^register/$', views.RegistrationView.as_view(),
        name='registration_register'),
    url(r'^', include('registration.urls')),
)
