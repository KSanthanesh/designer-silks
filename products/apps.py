""" Products apps.py"""
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """ Product Configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
