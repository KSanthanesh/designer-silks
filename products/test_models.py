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
        """Check the Name Field is str in Category class in products models"""

        category = Category.objects.create(
            name='chiffon_saree', friendly_name='Chiffon Saree')
        expected_string = str(category.name)
        self.assertEqual(str(category), expected_string)

    def test_product_method_returns(self):
        """ Check the Product class in product models """
        product = Product.objects.create(
            sku='ds1045670', name='Multicolour Saree', price=50.45,
            rating=4, length='Saree length is 5.5 m', material='silk',
            description='Lightweight', image='sis30003.jpg')
        self.assertEqual(str(product.sku), 'ds1045670')
        self.assertEqual(str(product.name), "Multicolour Saree")
        self.assertEqual(product.price, 50.45)
        self.assertEqual(product.rating, 4)
        self.assertEqual(str(product.length), 'Saree length is 5.5 m')
        self.assertEqual(str(product.material), 'silk')
        self.assertEqual(str(product.description), 'Lightweight')
        self.assertEqual(str(product.image), 'sis30003.jpg')
