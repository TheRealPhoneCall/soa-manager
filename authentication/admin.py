from django.contrib.auth import models as auth_models
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from hijack.admin import HijackUserAdminMixin

from .models import User


class CustomUserAdmin(UserAdmin):

    list_display = ['username', 'first_name', 'last_name', 'get_full_name', 'email', 'is_staff', 'is_superuser']


#admin.site.register(User, CustomUserAdmin)

# When using a custom User model, we need some workarounds for django-hijack
# See here: http://django-hijack.readthedocs.org/en/latest/troubleshooting/

#admin.site.unregister(User)


class CustomUserAdminWithHijackButton(HijackUserAdminMixin, CustomUserAdmin):
    """
    We are subclassing HijackUserAdminMixin to display the hijack button in the admin.
    """
    list_display = CustomUserAdmin.list_display + ['hijack_field', ]

admin.site.register(User, CustomUserAdminWithHijackButton)
