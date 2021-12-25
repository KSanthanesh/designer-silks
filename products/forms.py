""" Forms for product """
from django import forms
from products.models import Product, Category


class ProducForm(forms.ModelForm):
    """ For ProductForm """

    class Meta:
        """ Meta class for all the fields in ProductForm"""
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """ Using Init method to get friendly names in the categories"""
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attr['class'] = 'border-black rounded-0'
