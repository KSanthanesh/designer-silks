""" urls for profile page"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/', views.order_history,
         name='order_history'),
    path('order_history_view/<order_number>', views.order_history_view,
         name='order_history_view'),
    # path('order_review/<order_number>', views.review_rate, name='review_rate'),
]
