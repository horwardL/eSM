from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from catalogueApp.models import Product


def fetch_products(request, category_slug, market_slug):
    products_list = Product.objects.filter(product_status=0) 

    if category_slug != 'all-categories' and market_slug != 'all-markets':
        products_list = products_list.filter(categories__slug=category_slug, markets__slug=market_slug)

    if category_slug != 'all-categories' and market_slug == 'all-markets':
        products_list = products_list.filter(categories__slug=category_slug)

    if category_slug == 'all-categories' and market_slug != 'all-markets':
        products_list = products_list.filter(markets__slug=market_slug)
    
    page = request.GET.get('page', 1)

    paginator = Paginator(products_list, 9)

    try:
        page_object = paginator.page(page)
    except PageNotAnInteger:
        page_object = paginator.page(1)
    except EmptyPage:
        page_object = paginator.page(paginator.num_pages)
        
    return page_object