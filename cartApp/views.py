from django.shortcuts import render
from django.http import HttpRequest
from cartApp import cart_service
from datetime import datetime

def cart_detail(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        cart_service.remove_from_cart(request)

        return render(
            request,
            'cartApp/cart_detail.html',
            {
                'title': 'Cart Page',
                'year': datetime.now().year,
            }
        )
    else:
        return render(
            request,
            'cartApp/cart_detail.html',
            {
                'title': 'Cart Page',
                'year': datetime.now().year,
            }
        )