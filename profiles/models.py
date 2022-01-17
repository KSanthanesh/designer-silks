""" Userprofile models"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """ For users personal detais, order history and payment information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_address_line1 = models.CharField(
        max_length=50, null=True, blank=True)
    default_address_line2 = models.CharField(
        max_length=50, null=True, blank=True, default='')
    default_county_or_city = models.CharField(
        max_length=30, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True, default='')
    default_country = CountryField(
        blank_label='Country *', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update the User profile"""
    if created:
        UserProfile.objects.create(user=instance)

    # existing users: just save the profile
    instance.userprofile.save()
