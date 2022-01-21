""" Testing the products.models.py"""

from django.test import TestCase
from contact.models import Contact


class TestModels(TestCase):
    """ Test models for contact"""

    def test_contact_method_returns(self):
        """ Check the Contact class in contact """

        contact = Contact.objects.create(
            name='test', email='test@tes.com', subject='Test', newsletter='no')
        self.assertEqual(str(contact.name), 'test')
        self.assertEqual(str(contact.email), 'test@tes.com')
        self.assertEqual(str(contact.subject), 'Test')
        self.assertEqual(contact.newsletter, 'no')
