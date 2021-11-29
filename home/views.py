from django.shortcuts import render

# Create your views here.

def index(request):
    """
    A view to return the Home page
    """
    return render(request, 'home/index.html')
