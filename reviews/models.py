""" Review models.py """

from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """ User reviews and rating for the product details """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
