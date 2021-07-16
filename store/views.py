from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from carts.models import CartItem
from carts.views import _cart_id
from category.models import Category
from store.models import Product


# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 3)  # the products we want to show and number of products we want to show
        page = request.GET.get('page')  # /?page=2 we get page num from GET request
        paged_products = paginator.get_page(page)  # those 6 products get stored here

        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 3)  # the products we want to show and number of products we want to show
        page = request.GET.get('page')  # /?page=2 we get page num from GET request
        paged_products = paginator.get_page(page)  # those 6 products get stored here
        products_count = products.count()

    context = {
        'products': paged_products,
        'products_count': products_count
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),
                                          product=single_product).exists()  # checks the card model(foreign key of CartItem) and check that cart_id, exists returns True or False

    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
        'in_cart': in_cart
    }

    return render(request, 'store/product_detail.html', context)


def search(request):
    products = None
    products_count = 0
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword))  # looks anything related to keyword in description
            products_count = products.count()
    context = {
        'products': products,
        'products_count': products_count,
    }
    return render(request, 'store/store.html', context)
