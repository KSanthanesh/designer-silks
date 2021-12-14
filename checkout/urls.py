""" urls for checkout page"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
]