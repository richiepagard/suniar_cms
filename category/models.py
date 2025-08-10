from django.db import models


class Category(models.Model):
    """ Define model for categories. """
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
