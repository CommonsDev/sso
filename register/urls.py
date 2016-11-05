from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^$', views.ProfileView.as_view(), name='homepage'),  # alias
    url(r'^auth/$', views.EmailView.as_view(), name='auth'),
    url(r'^logout/$', views.LogoutView.as_view(), name='auth_logout'),
    # Keep 'registration.backends' URLs after '/auth/' and before 'auth_login'
    # for proper overriding.
    url(r'^', include('registration.backends.default.urls')),
    url(r'^auth/login/$', views.LoginView.as_view(), name='auth_login'),
    url(r'^auth/register/$', views.RegisterView.as_view(),
        name='auth_register'),
    url(r'^auth/profile/$', views.ProfileView.as_view(),
        name='register_profile'),
    url(r'^auth/activation/complete/$', views.ProfileView.as_view(),
        name='registration_activation_complete'),
]
