""" Checkout views.py """

from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from checkout.forms import OrderForm


def checkout(request):
    """ Check out page for orderdetail and payment section """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "The cart is empty at the moment.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JwkmnGvbFSZjLhHtro1nCBynY9WHol44qTfwckvo67VqjA27ZpRUBT85Uhp5gCRq8nhC0Uezd8ywbuSxFdVXJkH00DPmFJaxp',
        'client_secret': 'test client secret',
    }
    return render(request, 'checkout/checkout.html', context)
