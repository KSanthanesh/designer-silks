""" checkout.admin.py """

from django.contrib import admin
from checkout.models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    This Orderinline item is going to allow to add and edit line items
    in the admin
    """

    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Readonly fields, list-display and date in reverse chronological order
    """
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date', 'shipping_cost',
                       'order_total', 'grand_total', 'original_cart',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'address_line1', 'address_line2',
              'county_or_city', 'postcode', 'country', 'shipping_cost',
              'order_total', 'grand_total', 'original_cart', 'stripe_pid')

    list_display = ('order_number', 'user_profile', 'date', 'full_name',
                    'order_total', 'shipping_cost',  'grand_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
