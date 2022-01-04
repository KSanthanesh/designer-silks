""" Testing the products.models.py"""

from django.test import TestCase
from products.models import Product, Category


class TestModels(TestCase):
    """ Test models for category in products models"""

    def test_category_method_returns(self):
        """ Check the Category class in product models """

        category = Category.objects.create(
            name='chiffon_saree', friendly_name='Chiffon Saree')
        self.assertEqual(str(category.name), 'chiffon_saree')
        self.assertEqual(str(category.friendly_name), 'Chiffon Saree')

    def test_category_str_method_name_returns(self):
        """ 
        Check the Name Field is string in Category class in products models
        """
        category = Category.objects.create(
            name='chiffon_saree', friendly_name='Chiffon Saree')
        expected_string = str(category.name)
        self.assertEqual(str(category), expected_string)

    # def test_category_str_method_get_friendly_name_returns(self):
    #     """ 
    #     Check the Friendly Name Field is string in Category
    #     class in products models
    #     """
    #     category = Category.objects.GET(
    #         name='chiffon_saree', friendly_name='Chiffon Saree')
    #     expected_string = str(category.friendly_name)
    #     self.assertEqual(str(category), expected_string)


