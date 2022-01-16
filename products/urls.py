""" Products urls """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
    path('review_rate/<int:product_id>/', views.review_rate,
         name='review_rate'),
    path('wishlist/<int:product_id>/', views.wishlist, name='wishlist'),
    path('wishlist_history/', views.wishlist_history, name='wishlist_history'),
    path('wishlist_delete/<product_id>/', views.wishlist_delete,
         name='wishlist_delete'),
]
