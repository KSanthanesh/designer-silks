""" Testing the products.views.py"""

from django.test import TestCase


class TestViews(TestCase):
    """ Testing for Product Views"""

    # def test_add_product_page(self):
    #     """ Test for add product """
    #     response = self.client.get('/add/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'products/add_product.html')