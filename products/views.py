""" Products app views.py """

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.models import User

from products.models import Product, Category, Review, Wishlist
from products.forms import ProductForm, ReviewForm, WishlistForm


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
                products_list = products_list.annotate(
                    lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products_list = products_list.order_by(sortkey)

        if 'category' in request.GET:
            categories_list = request.GET['category'].split(',')
            products_list = products_list.filter(
                category__name__in=categories_list)
            categories_list = Category.objects.filter(name__in=categories_list)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter the search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products_list = products_list.filter(queries)

    current_sorting = f'{sort}_{direction}'
    if request.user.is_authenticated:
        list_wish = Wishlist.objects.filter(
            user=request.user).values_list('product', flat=True)
    else:
        list_wish = []
    context = {
        'products_list': products_list,
        'search_term': query,
        'current_categories': categories_list,
        'current_sorting': current_sorting,
        'wishlist': list_wish,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """User can view individual product details"""
    product = get_object_or_404(Product, pk=product_id)
    product_name = Product.objects.get(pk=product_id)

    review = Review.objects.filter(product=product_name)
    if request.user.is_authenticated:
        list_wish = Wishlist.objects.filter(
            user=request.user).values_list('product', flat=True)
    else:
        list_wish = []
    context = {
        'product': product,
        'review': review,
        'flg': 'wr',
        'wishlist': list_wish,
    }
    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add product to the website """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, Only store owners can do that")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added a Product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add a Product')
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'products/add_product.html', context)


def edit_product(request, product_id):
    """ Edit product to the website """

    if not request.user.is_superuser:
        messages.error(request, "Sorry, Only store owners can do that")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated a Product!')
            return redirect(reverse('product_detail', args=[product.id]))

        else:
            messages.error(request, 'Failed to update product.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')
    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'products/edit_product.html', context)


def delete_product(request, product_id):
    """ Delete product to the website """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, Only store owners can do that")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def review_rate(request, product_id):
    """ Reviews views"""
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added a Review")
            return redirect('product_detail', product_id)
        else:
            messages.error(request, "Failed to add, Please Enter Rating")

        form = ReviewForm()
        return redirect('product_detail', product_id)

    return redirect('product_detail', product_id)


def edit_r(request, p_id, r_id):
    """For Edit coloumn"""
    product = get_object_or_404(Product, pk=p_id)
    product_name = Product.objects.get(pk=p_id)

    review = Review.objects.filter(id=r_id)
    context = {
        'product': product,
        'review': review,
        'flg': 'er',
        'product_name': product_name,
    }
    return render(request, 'products/product_detail.html', context)


def edit_review(request, p_id, r_id):
    """ User can Edit their Reviews"""
    review = get_object_or_404(Review, id=r_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated a Review")
            return redirect('product_detail', p_id)
    form = ReviewForm(instance=review)

    return redirect('product_detail', p_id)


def delete_review(request, p_id, r_id):
    """ User can delete the their Reviews"""
    review = get_object_or_404(Review, id=r_id)
    review.delete()
    messages.info(request, "Successfully Deleted a Review")
    return redirect('product_detail', p_id)


def wishlist(request, product_id):
    """ Wishlist views"""
    wishlist_p = False
    product_name = Product.objects.get(pk=product_id)
    user_id = request.POST['user']
    wishlist_user = User.objects.get(pk=user_id)
    wishlist_p = Wishlist.objects.filter(
        product=product_name, user=wishlist_user).count()
    if wishlist_p < 1:

        if request.method == 'POST':
            form = WishlistForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Added a wishlist')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, "Failure to add")

            form = WishlistForm()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        wishlist_delete(request, product_id)
    user_id = request.user
    list_wish = Wishlist.objects.filter(user=user_id).values_list(
        'product', flat=True)
    context = {
        'wishlist': list_wish,
    }
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), context)


def wishlist_history(request):
    """Display Order History for specific order """

    user_id = request.user
    list_wish = Wishlist.objects.filter(user=user_id)
    context = {
        'wishlist': list_wish,
        'from_profile': True,
    }
    return render(request, 'products/wishlist.html', context)


def wishlist_delete(request, product_id):
    """ User can delete the wishlist from my wishlist page"""
    wishlist_p = Wishlist.objects.filter(product=product_id)

    wishlist_p.delete()
    messages.info(request, 'Removed from Wishlist')
    return redirect('wishlist_history')
