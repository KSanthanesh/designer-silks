""" Contact page models"""
from django.db import models


class Contact(models.Model):
    """ User can send enquiry"""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField()
    newsletter = models.TextField(default=0)

    def __str__(self):
        return str(self.name)
