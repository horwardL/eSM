from django.shortcuts import render, redirect
from django.http import HttpRequest
from datetime import datetime
from checkoutApp.forms import CheckoutForm
from checkoutApp.checkout_service import process_checkout

def checkout(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        result  = process_checkout(request)
        if result:
            return redirect('/checkout/receipt')
        else:
            return redirect('/checkout/receipt')
    else:
        form = CheckoutForm()
        return render(
            request,
            'checkoutApp/checkout.html',
            {
                'title':'Checkout Page',
                'year':datetime.now().year,
                'form': form,
                }
        )

def receipt(request):
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'checkoutApp/receipt.html',
        {
            'title':'Receipt Page',
            'year':datetime.now().year,
        }
    )
