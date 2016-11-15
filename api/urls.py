from django.conf.urls import url

from .views import ProfileView


urlpatterns = [
    url(r'^profile/', ProfileView.as_view())
]
