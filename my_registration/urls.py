from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^accounts/register/$', views.MyRegistrationView.as_view(), name='registration_register'),  # This will override the original registration_register
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
