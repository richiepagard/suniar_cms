from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Represents users in the project, customize default user model.

    Arguments:
        phone_numbe (str): Unique phone number to authenticate the user.
        username (str): Unique username to identify and display name of user.
        email (str): Unique email address to authenticate with email for account.
        first_name (str): User's first name.
        last_name (str): User's last name.
        is_active (bool): The activation status of user.
        is_staff (bool): The staff mode of a user, same as admin users.
        role (str): User's specific role.
    """
    class Role(models.TextChoices):
        user = "user", "Normal User"
        super_user = "super_user", "Super User"
        programmer = "programmer", "Programmer"
        ceo = "ceo", "CEO"

    phone_number = PhoneNumberField(
        region="IR",
        unique=True,
        verbose_name=_("Phone number")
    )
    username = models.CharField(
        max_length=30,
        unique=True,
        verbose_name=_("Username")
    )
    email = models.EmailField(
        unique=True,
        null=True,
        blank=True,
        verbose_name=_("Email")
    )
    first_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("First name")
    )
    last_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Last name")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Activation status")
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("Staff situation")
    )
    role = models.CharField(
        max_length=12,
        choices=Role.choices,
        default=Role.user,
        verbose_name=_("Role")
    )

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self) -> str:
        return f"{self.phone_number} - {self.username}"
