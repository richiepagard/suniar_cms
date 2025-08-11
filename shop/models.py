from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from category.models import Category


class Shop(models.Model):
    """
    Define shop details and models.
    """
    name = models.CharField(
        max_length=255,
        unique=True
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='shop_owner'
    )
    members = models.ManyToManyField(
        get_user_model(),
        related_name='shop_user',
        blank=True
    )
    work_field = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    created_at = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=False)
    categories = models.ManyToManyField(
        Category,
        blank=True
    )

    def __str__(self):
        """ Return Shop name. """
        return f"{self.name} - {self.owner}"
