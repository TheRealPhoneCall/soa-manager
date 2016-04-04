from django.core.urlresolvers import reverse

from registration.backends.simple.views import RegistrationView

from .forms import MyRegistrationForm


# By extending RegistrationView we can customize the registration process
# http://django-registration-redux.readthedocs.org/en/latest/views.html#registration.views.RegistrationView

class MyRegistrationView(RegistrationView):

    form_class = MyRegistrationForm

    def get_success_url(self, request, user):
        return reverse('soamgr:home')
