from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^auth/', include('oauth.urls', namespace='oauth2_provider')),
    # Using simple backend registration (no email confirmation). See
    # https://django-registration.readthedocs.org/en/latest/simple-backend.html
    (r'^registration/', include('register.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('default.urls')),
)
