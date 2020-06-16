from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime


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
        return render(
            request,
            'catalogueApp/index.html',
            {
                'title': 'Product Page',
                'year': datetime.now().year,
            }
        )


def product_detail(args):
    return render()