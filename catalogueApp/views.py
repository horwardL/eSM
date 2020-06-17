from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from catalogueApp.catalogue_service import fetch_product

def catalogue(request, category_slug='all-categories', market_slug='all-markets'):
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        page_object = fetch_product(request, category_slug, market_slug)
        return render(
            request,
            'catalogueApp/index.html',
            {
                'title': 'Product Page',
                'year': datetime.now().year,
                'page_object': page_object,
                'selected_category': category_slug,
                'selected_market': market_slug,
            }
        )
    else:
        page_object = fetch_product(request, category_slug, market_slug)
        return render(
            request,
            'catalogueApp/index.html',
            {
                'title': 'Product Page',
                'year': datetime.now().year,
                'page_object': page_object,
                'selected_category': category_slug,
                'selected_market': market_slug,
            }
        )


def product_detail(args):
    return render()