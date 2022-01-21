""" Testing the views.py """

from django.test import TestCase


class TestViews(TestCase):
    """ TestViews """
    def test_contact(self):
        """ Contact page Testing """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
