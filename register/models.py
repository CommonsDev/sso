from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, is_staff, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_active=True,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, null=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_short_name(self):
        return self.email

    def has_module_perms(self, *args):
        return self.is_staff

    def has_perm(self, *args):
        return self.is_staff
