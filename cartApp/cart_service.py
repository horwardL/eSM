import uuid
from catalogueApp.models import Product
from cartApp.models import Cart, CartItem
from django.shortcuts import get_object_or_404
import decimal

UNIQUE_CART_ID_SESSION_KEY = 'unique_cart_id'


def _unique_cart_id(request):
     if request.session.get(UNIQUE_CART_ID_SESSION_KEY,'') == '':            
         request.session[UNIQUE_CART_ID_SESSION_KEY] = _generate_unique_id()    
     return request.session[UNIQUE_CART_ID_SESSION_KEY]


def _generate_unique_id():
    u_id = uuid.uuid1()
    u_id_string = str(u_id)
    return u_id_string

def get_cart(request): 
    unique_id =_unique_cart_id(request)
    try:
        cart = get_object_or_404(Cart, unique_cart_id=unique_id)
        return cart
    except :
        return None

def add_to_cart(request):

    postdata = request.POST.copy()
    product_id = postdata['product_id']
    
    product = get_object_or_404(Product, id=product_id)
    
    cart = get_cart(request)
 
    if cart:
        try:
           cart_item = get_object_or_404(CartItem, cart=cart, product__id=product_id)
        except:
           cart_item = None

        if cart_item:          
            cart_item.increase_quantity(1)
        else:
            new_cart_item = CartItem()
            new_cart_item.quantity = 1
            new_cart_item.product = product
            new_cart_item.cart = cart
            new_cart_item.save()
    else:
        new_cart = Cart()
        new_cart.unique_cart_id = _unique_cart_id(request)
        new_cart.save()

        new_cart_item = CartItem()
        new_cart_item.quantity = 1
        new_cart_item.product = product
        new_cart_item.cart = new_cart
        new_cart_item.save()

def remove_from_cart(request):
    postdata = request.POST.copy()
    product_id = postdata['product_id']
    cart_item = CartItem.objects.filter(product__id=product_id)
    cart_item.delete()

def get_cart_items(request):
    cart = get_cart(request)

    if cart:
        return CartItem.objects.filter(cart__unique_cart_id=_unique_cart_id(request))

def cart_items_count(request):
    items = get_cart_items(request)
    cnt = 0
    if items:     
       for item in items:
           cnt += item.quantity
    return cnt

def get_cart_total(request):
    cart = get_cart(request)
    cart_total = decimal.Decimal('0.00')

    if cart:
        cart_items = CartItem.objects.filter(cart__unique_cart_id=_unique_cart_id(request))
        for item in cart_items:
            cart_total += item.cart_item_total()
        return cart_total
    else:
        return cart_total
