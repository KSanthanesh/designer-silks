""" Home views.py"""
from django.shortcuts import render


def index(request):
    """
    A view to return the Home page
    """
    return render(request, 'home/index.html')
