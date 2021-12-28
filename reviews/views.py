"""Views for Reviews"""

from django.shortcuts import redirect
from reviews.models import Review
from products.models import Product


def review_rate(request):
    """ Reviews views"""
    if request.method == "GET":
        product_id = request.GET.get('product_id')
        product = Product.objects.get(id=product_id)
        comment = request.GET.get('comment')
        rate = request.GET.get('rate')
        user = request.user

        Review(user=user, product=product, comment=comment, rate=rate).save()

        return redirect('product_detail', id=product_id)
        # return render(request, 'products/products.html')
