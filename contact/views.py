""" Views for contact page"""

from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def contacts(request):
    """ User can send enquiry in the contact page"""
    # contact = get_object_or_404(Contact)
    if request.method == "POST":
        form = ContactForm(request.POST)
        form.save()
        # if form.is_valid():
        #     form.save()
        #     name = request.POST['name']
        #     if name == "guest":
        #         messages.success(request, 'Thanks for Subscribing Newletter')
        #         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # else:
        # messages.success(request, 'Thanks for Contact Us!')

    form = ContactForm()
    # context = {
    #     'form': form,
    #     'contact': contact,
    # }
    messages.success(request, 'Thanks for Contact Us!')
    return render(request, 'contact/contact.html')
