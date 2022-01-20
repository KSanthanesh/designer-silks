""" Profile apps.py"""
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """ Profiles configuration """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
