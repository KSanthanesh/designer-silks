""" for checkout models"""
import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """ User order details regarding shipping"""
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address_line1 = models.CharField(max_length=50, null=False, blank=False)
    address_line2 = models.CharField(
        max_length=50, null=True, blank=True, default='')
    county_or_city = models.CharField(max_length=30, null=False, blank=False)
    postcode = models.CharField(
        max_length=20, null=True, blank=True, default='')
    country = CountryField(blank_label='Country *', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    shipping_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """ Generate a Unique random number using uuid """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Update grand total each time a line is added,
        accounting for shipping costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_SHIPPING_THRESHOLD:
            self.shipping_cost = (
                self.order_total * settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        else:
            self.shipping_cost = 0
        self.grand_total = self.order_total + self.shipping_cost
        self.save()

    def save(self, *args, **kwargs):
        """ Override the original save method to set the Order Number """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """ Orderline Item """

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=False,
        blank=False, related_name='lineitems')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False,
        editable=False)

    def save(self, *args, **kwargs):
        """ Override the original save method to set the LineItem total
        and update the order total.
         """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU{self.product.sku} on order {self.order.order_number}'
