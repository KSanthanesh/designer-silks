""" Reviews admin"""

from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Display Reviews and rating """
    list_display = ('user', 'product', 'rate', 'created_at',)

    readonly_fields = ['created_at']
