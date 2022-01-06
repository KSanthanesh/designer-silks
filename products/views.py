""" Products app views.py """

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.models import User
from profiles.models import UserProfile

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
    product_name = Product.objects.get(pk=product_id)
    # review = get_object_or_404(Review, product=product_name)
    review = Review.objects.filter(product=product_name)
    context = {
        'product': product,
        'review': review,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
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


@login_required
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


@login_required
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
        # products = request.POST['rate']
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added a Review")
            return redirect('product_detail', product_id)
        else:
            messages.error(request, "Failed to add, Please Enter Rating")

        form = ReviewForm()
        return redirect('product_detail', product_id)
    # if request.method == "GET":
    #     product_id = request.GET.get('product')
    #     product = Product.objects.get(pk=product_id)
    #     comment = request.GET.get('comment')
    #     rate = request.GET.get('rate')
    #     user = request.GET.get('user')
    #     created_at = request.GET.get('created_at')

    #     Review(user=user, product=product, comment=comment, rate=rate).save()

    return redirect('product_detail', product_id)


def wishlist(request, product_id):
    """ Wishlist views"""
    wishlist_p = "None"
    product_name = Product.objects.get(pk=product_id)
    user_id = request.POST['user']
    wishlist_user = User.objects.get(pk=user_id)
    wishlist_p = Wishlist.objects.filter(product=product_name, user=wishlist_user).count()
    if wishlist_p < 1:

        if request.method == 'POST':
            form = WishlistForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully added a wishlist')
                return redirect('products')
            else:
                messages.error(request, "Failure to add")

            form = WishlistForm()
            return redirect('products')
    else:
        messages.warning(request, 'Already in Your Wishlist')
    return redirect('products')


def wishlist1(request, product_id):
    """ Wishlist views"""
    wishlist_p = "None"
    product_name = Product.objects.get(pk=product_id)
    user_id = request.POST['user']
    wishlist_user = User.objects.get(pk=user_id)
    wishlist_p = Wishlist.objects.filter(product=product_name, user=wishlist_user).count()
    if wishlist_p < 1:

        if request.method == 'POST':
            form = WishlistForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully added a wishlist')
                return redirect('product_detail', product_id)
            else:
                messages.error(request, "Failure to add")

            form = WishlistForm()
            return redirect('product_detail', product_id)
    else:
        messages.warning(request, 'Already in Your Wishlist')
    return redirect('product_detail', product_id)


def wishlist_history(request):
    """Display Order History for specific order """
    profileuser = get_object_or_404(UserProfile, user=request.user)
    # order = get_object_or_404(Order, user_profile=request.user)
    # wishlist = profileuser.wishlist.all()
    wishlist = Wishlist.objects.all()

    # messages.info(request, f'Your order Number is {order}.')
    context = {
        'wishlist': wishlist,
        'from_profile': True,
    }
    
    return render(request, 'products/wishlist.html', context)


def wishlist_delete(request, product_id):
    # wishlists = get_object_or_404(Wishlist, product=product_id)
    # product_name = Wishlist.objects.filter(pk=product_id)
    # product_name = Product.objects.get(pk=product_id)
    wishlist_p = Wishlist.objects.filter(product=product_id)
    
    wishlist_p.delete()
    messages.success(request, 'Deleted Successfully')
    return redirect('wishlist_history')

