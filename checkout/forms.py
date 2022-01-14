""" Checkout OrderForm """

from django import forms
from checkout.models import Order


class OrderForm(forms.ModelForm):
    """ OrderForm for User details"""
    class Meta:
        """ for personal detail and address"""
        model = Order
        fields = ('full_name', 'email', 'phone_number', 'address_line1',
                  'address_line2', 'county_or_city', 'postcode', 'country',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove re-generated lables and
        set autofocus
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'address_line1': 'Street Name',
            'address_line2': 'Street Name(Optional)',
            'county_or_city': 'County or City',
            'postcode': 'Postcode(Optional)',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]}*'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
