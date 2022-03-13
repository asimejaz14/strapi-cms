from django.db import models


# Create your models here.
class Status(models.Model):
    """
    Model for department status
    i.e, Active, Inactive
    """

    name = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name