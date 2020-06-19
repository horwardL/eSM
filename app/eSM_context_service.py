from eSM import settings
from catalogueApp.models import Market, Category
from cartApp import cart_service

def eSM_context(request):
    return {
        'site_name': settings.SITE_NANE,

        'categories': Category.objects.filter(category_status=0),
        'markets': Market.objects.filter(market_status=0),
        'selected_category': 'all-categories',
        'selected_market': 'all-markets',

        'cart_item_count': cart_service.cart_items_count(request),
        'cart_total': cart_service.get_cart_total(request),
        'cart_items': cart_service.get_cart_items(request),
    }