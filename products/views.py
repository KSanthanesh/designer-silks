""" Products app views.py """

from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """User can view all products including sorting and search the products """
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """User can view individual product details"""
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
