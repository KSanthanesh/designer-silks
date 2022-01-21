"""
Testcase for forms.py
"""
from django.test import TestCase
from .forms import ContactForm

# Create your tests here.


class TestContactForm(TestCase):
    """
    For Contact Form
    """

    def test_user_name_is_required(self):
        """
        User name is required
        """
        form = ContactForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(
            form.errors['name'][0], 'This field is required.')

    def test_user_email_is_required(self):
        """
        User email is required
        """
        form = ContactForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_subject_is_required(self):
        """
        Subject is required
        """
        form = ContactForm({'subject': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors.keys())
        self.assertEqual(
            form.errors['subject'][0], 'This field is required.')

    def test_newsletter_is_required(self):
        """
        Newsletter subscription  is required
        """
        form = ContactForm({'newsletter': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('newsletter', form.errors.keys())
        self.assertEqual(
            form.errors['newsletter'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        For meta fields
        """
        form = ContactForm()
        self.assertEqual(form.Meta.fields, '__all__')
