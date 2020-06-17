from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from catalogueApp.catalogue_service import fetch_product

def catalogue(request, catagory_slug='all-categories', market_slug='all-brands'):
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        return render(
            request,
            'catalogueApp/index.html',
            {
                'title': 'Product Page',
                'year': datetime.now().year,
            }
        )
    else:
        page_object = fetch_product(request, catagory_slug, market_slug)

        return render(
            request,
            'catalogueApp/index.html',
            {
                'title': 'Product Page',
                'year': datetime.now().year,
                'page_object': page_object,
            }
        )


def product_detail(args):
    return render()