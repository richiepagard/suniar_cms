from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager

)

from django.db import models


class UserManager(BaseUserManager):
    """ Manage for Users."""

    def create_user(self, email, password, **extra_fields):
        """ Create,Save and return a user. """
        # if not email:
        #     raise ValueError('Email field is necessary')
        # email = self.normalize_email(email)
        # user = self.model(email=email, **extra_fields)
        # user.set_password(password)
        # user.save(using=self._db)
        #
        # return user
        if not email:
            raise ValueError('Email field is necessary')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password):
        """ Create and save a superuser. """
        user = self.create_user(email, password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ User in the system. """

    class Role(models.TextChoices):
        user = "user", "Normal User"
        super_user = "super_user", "Super User"
        programmer = "programmer", "Programmer"
        ceo = "ceo", "CEO"

    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    mobile = models.CharField(max_length=11, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=12, choices=Role.choices, default=Role.user)

    # role = models.CharField(choices=
    # [
    #     ('user', 'Normal User'),
    #     ('super_user', 'Super User'),
    #     ('programmer', 'Programmer'),
    #     ('ceo', 'CEO')
    # ],
    #     default=models.Choices
    # )

    objects = UserManager()

    USERNAME_FIELD = 'email'
