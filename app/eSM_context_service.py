from eSM import settings
from catalogueApp.models import Category, Market

def eSM_context(request):
    return {
        'site_name': settings.SITE_NANE,
        'categories': Category.objects.filter(category_status=0),
        'markets': Market.objects.filter(market_status=0)
    }