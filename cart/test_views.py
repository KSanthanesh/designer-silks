""" Testing the views.py """

from django.test import TestCase


class TestViews(TestCase):
    """ TestViews """
    def test_cart(self):
        """ Cart page Testing """
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')
