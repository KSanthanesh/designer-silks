""" urls for reviews"""

from django.urls import path
from . import views

urlpatterns = [
    path('reviews', views.review_rate, name='review_rate'),
]
