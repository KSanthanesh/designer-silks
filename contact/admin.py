""" Adding contact in admin page"""
from django.contrib import admin
from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    """Display list for Contact in the admin page """

    list_display = ('name', 'email', 'subject')


admin.site.register(Contact, ContactAdmin)
