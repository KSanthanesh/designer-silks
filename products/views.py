""" Products app views.py """

from django.shortcuts import render
from .models import Product


def all_products(request):
    """User can view all products including sorting and search the products """
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
