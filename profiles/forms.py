""" Profiles form """

from django import forms
from profiles.models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ for User details"""
    class Meta:
        """ for personal details, address and order confirmation"""
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders and classes, remove re-generated lables and
        set autofocus
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_address_line1': 'Street Name',
            'default_address_line2': 'Street Name(Optional)',
            'default_county_or_city': 'County or City',
            'default_postcode': 'Postcode(Optional)',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]}*'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'border-black rounded-0 profile-input')
            self.fields[field].label = False
