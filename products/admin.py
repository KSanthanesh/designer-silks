""" For Superuser"""

from django.contrib import admin
from products.models import Product, Category, Review, Wishlist


class ProductAdmin(admin.ModelAdmin):
    """ Display list for Products in the admin page """

    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'material',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """ Display list for Category in the admin page """

    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    """Display list for Review in the admin page """

    list_display = ('user', 'product', 'comment', 'rate', 'created_at')


class WishlistAdmin(admin.ModelAdmin):
    """Display list for Wishlist in the admin page """
    list_display = ('user', 'product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)
