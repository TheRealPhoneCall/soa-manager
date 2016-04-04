from django.contrib.auth.models import AbstractUser
from django.db import models


from lib.values import GROUP_HUMAN


class User(AbstractUser):  # I would prefer to call it CustomUser but then the database tables look funny

    @property
    def group_human(self):
        groups = self.groups.all()
        group_name = groups[0].name if groups else None
        group_human = GROUP_HUMAN.get(group_name, 'n.a.')
        return group_human
