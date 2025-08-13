from django.db import models
from django.db.models.fields import DateTimeField
from django.utils.translation import gettext_lazy as _

from category.models import Category


class Product(models.Model):
    """
    Represents Product model that we want to present in project.

    Arguments:
        name (str): represents name of the product.
        categories (str): it`s a M2M relation that Define the type and category of a product we want to present.
        price (decimal): the value and price of a product must pay.
        is_active (bool): see if product is active or not.
        created_at (datetime): the time that product has been created.
        updated_at (datetime): the time that product has been updated.
    """
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name= _('Product name')
    )
    categories = models.ManyToManyField(
        Category,
        blank=True,
        verbose_name=_('Product Categories')
    )
    price=models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Product Price')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Activation Status')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created Time')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated time')
    )

