""" Profiles views """

from django.shortcuts import render


def profile(request):
    """ Display the User details, order and payment confirmation"""

    return render(request, 'profiles/profile.html')
