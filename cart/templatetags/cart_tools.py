""" Calculating subtotal"""

from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculating product price * product quantity """
    return price * quantity
