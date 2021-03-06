""" Product models database """

from django.db import models
from django.contrib.auth.models import User


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

    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True)
    sku = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    material = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    length = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Review(models.Model):
    """ User reviews and rating for the product details """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Wishlist(models.Model):
    """ User can add wishlist from the products"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
