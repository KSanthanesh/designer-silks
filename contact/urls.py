""" urls for contact page"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacts, name='contacts'),
]
