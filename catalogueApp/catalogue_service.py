from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from catalogueApp.models import Product


def fetch_product(request, category_slug, market_slug):
    products_list = Product.objects.filter(product_status=0)

    if category_slug != 'all-categories' and market_slug != 'all-markets':
        products_list = Product.objects.filter(category_slug=category_slug, market_slug=market_slug)
    
    if category_slug != 'all-categories' and market_slug == 'all-markets':
        products_list = Product.objects.filter(category_slug=category_slug)

    if category_slug == 'all-categories' and market_slug != 'all-markets':
        products_list = Product.objects.filter(market_slug=market_slug)

    page = request.GET.get('page', 1)

    paginator = Paginator(products_list, 9)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    return products