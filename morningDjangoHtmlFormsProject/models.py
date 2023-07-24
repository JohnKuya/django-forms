from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    qtty = models.CharField(max_length=30, blank=False, null=False)
    size = models.CharField(max_length=30, blank=False, null=False)
    price = models.CharField(max_length=30, blank=False, null=False)


def __str__(selpf):
    return self.home
