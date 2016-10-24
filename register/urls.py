from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^activate/complete/$',
        views.NextRedirectView.as_view(),
        name='registration_activation_complete'),
    url(r'^register/profile/$', views.ProfileView.as_view(),
        name='register_profile'),
    url(r'^register/$', views.RegistrationView.as_view(),
        name='registration_register'),
    url(r'^', include('registration.backends.default.urls')),
]
