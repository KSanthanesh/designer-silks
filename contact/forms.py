""" Contact forms.py """
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact form for contact page
    """

    class Meta:
        """
        Class Meta
        """
        model = Contact
        fields = '__all__'
