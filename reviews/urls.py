""" urls for reviews"""

from django.urls import path
from . import views

urlpatterns = [
    path('reviews/<int:product_id>/', views.review_rate, name='review_rate'),
]
