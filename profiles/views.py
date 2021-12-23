""" Profiles views """

from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from profiles.models import UserProfile
from profiles.forms import UserProfileForm


def profile(request):
    """ Display the User details, order and payment confirmation"""

    profileuser = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.Post, instance=profileuser)

        if form.is_valid:
            form.save()
            messages.success(request, "Profiles Updated Successfully.")

    form = UserProfileForm(instance=profileuser)
    orders = profileuser.orders.all()

    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, 'profiles/profile.html', context)
