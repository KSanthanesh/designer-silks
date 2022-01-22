""" Views for contact page"""

from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def contacts(request):
    """ User can send enquiry in the contact page"""
    if request.method == "POST":
        form = ContactForm(request.POST)
        form.save()
        messages.success(request, 'Thanks for Contact Us!')

    form = ContactForm()
    return render(request, 'contact/contact.html')
