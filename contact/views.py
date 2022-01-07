""" Views for contact page"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm


def contacts(request):
    """ User can send enquiry in the contact page"""
    contact = get_object_or_404(Contact)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("<h1>Thanks for Contact Us</h1>")
    form = ContactForm()
    context = {
        'form': form,
        'contact': contact,
    }

    return render(request, 'contact/contact.html', context)
