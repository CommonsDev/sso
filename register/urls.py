from django.conf.urls import include, url

from . import views


urlpatterns = [
        name='registration_activation_complete'),
    url(r'^logout/$', views.LogoutView.as_view(), name='auth_logout'),
    url(r'^login/$', views.EmailView.as_view(), name='auth_email'),
    # Keep 'registration.backends' URLs after '/login/' and before 'auth_login'
    # for proper overriding.
    url(r'^', include('registration.backends.default.urls')),
    url(r'^auth/login/$', views.LoginView.as_view(), name='auth_login'),
    url(r'^auth/register/$', views.RegisterView.as_view(), name='auth_register'),
    url(r'^activate/complete/$', views.NextRedirectView.as_view(),
    url(r'^register/profile/$', views.ProfileView.as_view(),
        name='register_profile'),
    url(r'^register/$', views.RegistrationView.as_view(),
        name='registration_register'),
]
