""" Products app views.py """

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from products.models import Product, Category
from products.forms import ProductForm


def all_products(request):
    """User can view all products including sorting and search the products """
    products_list = Product.objects.all()
    query = None
    categories_list = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products_list = products_list.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products_list = products_list.order_by(sortkey)

        if 'category' in request.GET:
            categories_list = request.GET['category'].split(',')
            products_list = products_list.filter(category__name__in=categories_list)
            categories_list = Category.objects.filter(name__in=categories_list)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter the search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)  # noqa: E501
            products_list = products_list.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products_list': products_list,
        'search_term': query,
        'current_categories': categories_list,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """User can view individual product details"""
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add product to the website """
    form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'products/add_product.html', context)
