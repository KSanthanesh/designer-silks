""" Checkout views.py """

import json
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

import stripe

from checkout.forms import OrderForm
from products.models import Product
from cart.contexts import cart_contents
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from .models import Order, OrderLineItem


@require_POST
def cache_checkout_data(request):
    """ For cache checkout data """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as exception:
        messages.error(request, 'Sorry, Your payment cannot be processed \
            right now. Please try again later')
        return HttpResponse(content=exception, status=400)


def checkout(request):
    """ Check out page for orderdetail and payment section """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'county_or_city': request.POST['county_or_city'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasnot found \
                        in our database." "Please call us for assistance")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "The cart is empty at the moment.")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        cart_total = current_cart['grand_total']
        stripe_total = round(cart_total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY

        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'address_line1': profile.default_address_line1,
                    'address_line2': profile.default_address_line2,
                    'county_or_city': profile.default_county_or_city,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                })

            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Check if you have set it in your environment?')

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    """
    To handle success checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profiles to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_address_line1': order.address_line1,
                'default_address_line2': order.address_line2,
                'default_county_or_city': order.county_or_city,
                'default_postcode': order.postcode,
                'default_country': order.country,
            }

            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Your Order successfully processed! \
        Your Order Number is {order_number}. A Confirmation \
        Email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']
        context = {
            'order': order
        }
        return render(request, 'checkout/checkout_success.html', context)
