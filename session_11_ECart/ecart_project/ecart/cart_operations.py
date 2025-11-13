from decimal import Decimal
from django.conf import settings
from .models import Product

# Key for session
CART_SESSION_ID = 'cart'

# get cart dict from session
def get_cart(request):
    return request.session.get(CART_SESSION_ID, {})

# save cart back to session
def save_cart(request, cart):
    request.session[CART_SESSION_ID] = cart
    request.session.modified = True

# add item to cart
def add_to_cart(request, product_id, quantity=1):
    cart = get_cart(request)
    product = Product.objects.get(id=product_id)
    product_id = str(product.id)
    if product_id not in cart:
        cart[product_id] = {'quantity': 0, 'price': str(product.price), 'name': product.name}
    cart[product_id]['quantity'] += quantity
    save_cart(request, cart)

# remove item
def remove_from_cart(request, product_id):
    cart = get_cart(request)
    product_id = str(product_id)
    if product_id in cart:
        del cart[product_id]
        save_cart(request, cart)

# get cart total + items
def cart_summary(request):
    cart = get_cart(request)
    items = []
    total = Decimal('0.00')
    for product_id, data in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            subtotal = Decimal(data['price']) * data['quantity']
            items.append({
                'product': product,
                'quantity': data['quantity'],
                'subtotal': subtotal,
            })
            total += subtotal
        except Product.DoesNotExist:
            continue
    return {'items': items, 'total': total}
