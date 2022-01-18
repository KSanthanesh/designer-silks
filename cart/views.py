""" Views for cart app """

from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """
    A view to return the cart page
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add a quantity of the specified product to the cart
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        if quantity == 1:
            messages.success(
                request, f'Updated {cart[item_id]} quantity of {product.name}')
        else:
            messages.success(
                request,
                f'Updated {cart[item_id]} quantity of {product.name}s')
    else:
        cart[item_id] = quantity
        if quantity == 1:
            messages.success(
                request, f'{product.name} succesfully added in your Cart')
        else:
            messages.success(
                request, f'{product.name}s succesfully added in your Cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust the quantity in the cart
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        if quantity == 1:
            messages.success(
                request, f'Updated {cart[item_id]} quantity of {product.name}')
        else:
            messages.success(
                request,
                f'Updated {cart[item_id]} quantity of {product.name}s')
    else:
        cart.pop(item_id)
        if quantity == 1:
            messages.success(request, f'{product.name} Removed from your Cart')
        else:
            messages.success(
                request, f'{product.name}s Removed from your Cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    remove the quantity from cart
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        messages.success(request, f'{product.name} Removed from your Cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error Removing item: {e}')
        return HttpResponse(status=500)
