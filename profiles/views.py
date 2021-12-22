""" Profiles views """

from django.shortcuts import render, get_object_or_404
from profiles.models import UserProfile


def profile(request):
    """ Display the User details, order and payment confirmation"""
    profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        'profile': profile,
    }

    return render(request, 'profiles/profile.html', context)
