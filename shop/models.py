from django.conf import settings
from django.db import models

# Create your models here.
class Shop(models.Model):
    """ Define shop details and models. """
    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='shop-owner'
    )
    work_field = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        """ Return Shop name. """
        return self.name
