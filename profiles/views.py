""" Profiles views """

from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from checkout.models import Order


def profile(request):
    """ Display the User details, order and payment confirmation"""

    profileuser = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profileuser)

        if form.is_valid:
            form.save()
            messages.success(request, "Profiles Updated Successfully.")
        else:
            messages.error(request, 'Update Failed.')
    else:
        form = UserProfileForm(instance=profileuser)
    orders = profileuser.orders.all()

    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, 'profiles/profile.html', context)


def order_history(request, order_number):
    """Display Order History for specific order """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, f'Your order Number is {order_number}.')
    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, 'checkout/checkout_success.html', context)
