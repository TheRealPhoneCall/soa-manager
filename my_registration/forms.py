from collections import OrderedDict

from django import forms

from registration.forms import RegistrationForm


def split_full_name(full_name):
    if not full_name:
        first_name, last_name = '', ''
    else:
        parts = full_name.split(' ')
        if len(parts) == 1:
            first_name = parts[0]
            last_name = ''
        elif len(parts) == 2:
            first_name = parts[0]
            last_name = parts[1]
        else:
            first_name = parts[0]
            last_name = ' '.join(parts[1:])
    return first_name, last_name


class MyRegistrationForm(RegistrationForm):

    first_name = forms.CharField(required=False, widget=forms.HiddenInput())
    last_name = forms.CharField(required=False, widget=forms.HiddenInput())
    full_name = forms.CharField(required=True)

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        first_name, last_name = split_full_name(full_name)
        self.instance.first_name = first_name
        self.instance.last_name = last_name
        return full_name

# Hack to define the field order
#   See here: http://stackoverflow.com/a/27595191/647991
MyRegistrationForm.base_fields = OrderedDict(
    (k, MyRegistrationForm.base_fields[k])
    for k in ['first_name', 'last_name', 'full_name', 'username', 'email', 'password1', 'password2']
)
