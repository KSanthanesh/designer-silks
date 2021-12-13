""" Product models database """

from django.db import models


class Category(models.Model):
    """ Saree Category"""

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """ Friendly name for the Product Display"""
        return str(self.friendly_name)

    class Meta:
        """ Meta Class """
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    """Product details database"""

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)  # noqa: E501
    sku = models.CharField(max_length=50, blank=True, default=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # noqa: E501
    material = models.CharField(max_length=50, blank=True, default=True)
    description = models.TextField(max_length=254, blank=True, default=True)
    length = models.CharField(max_length=50, blank=True, default=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
