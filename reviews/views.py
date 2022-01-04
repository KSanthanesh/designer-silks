"""Views for Reviews"""

from django.shortcuts import redirect
from reviews.models import Review
from products.models import Product


def review_rate(request, product_id):
    """ Reviews views"""
    if request.method == "GET":
        product_id = request.GET.get('product_id')
        product = Product.objects.get(pk=product_id)
        comment = request.GET.get('comment')
        rate = request.GET.get('rate')
        user = request.user

        Review(user=user, product=product, comment=comment, rate=rate).save()

    return redirect('product_detail', product_id)
