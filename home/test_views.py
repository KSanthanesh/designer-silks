""" Testing the views.py """

from django.test import TestCase


class TestViews(TestCase):
    """ TestViews """
    def test_home(self):
        """ Home page Testing """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
