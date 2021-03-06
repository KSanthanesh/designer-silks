""" Forms for product """
from django import forms
from products.widgets import CustomClearableFileInput
from products.models import Product, Category, Review, Wishlist


class ProductForm(forms.ModelForm):
    """ For ProductForm """

    class Meta:
        """ Meta class for all the fields in ProductForm"""
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """ Using Init method to get friendly names in the categories"""
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names


class ReviewForm(forms.ModelForm):
    """ Using form for Review comment and Star rating"""
    class Meta:
        """Meta class for ReviewForm"""
        model = Review
        fields = '__all__'


class WishlistForm(forms.ModelForm):
    """ Using form for Wishlist"""
    class Meta:
        """Meta class for Wishlist"""
        model = Wishlist
        fields = '__all__'
