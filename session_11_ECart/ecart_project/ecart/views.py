from django.shortcuts import render, get_object_or_404
from .models import Product, Category,Order,CartItem,Review
from .forms import CheckoutForm,ReviewForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .forms import RegisterForm


# Home page / Product list
def home(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()
    return render(request, 'ecart/home.html', {'products': products, 'categories': categories})

# Category-based list (optional)
def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_active=True)
    return render(request, 'ecart/category_products.html', {'category': category, 'products': products})

# Product detail page

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    reviews = Review.objects.filter(product=product).order_by('-created_at')
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            if request.user.is_authenticated:
                review.user = request.user
            review.save()
            return redirect('ecart:product_detail', slug=slug)

    return render(request, 'ecart/product_detail.html', {'product': product, 'form': form, 'reviews': reviews})

from django.shortcuts import redirect
from .cart_operations import add_to_cart, remove_from_cart, cart_summary

def add_cart_view(request, product_id):
    add_to_cart(request, product_id)
    return redirect('ecart:view_cart')

def remove_cart_view(request, product_id):
    remove_from_cart(request, product_id)
    return redirect('ecart:view_cart')

def view_cart(request):
    data = cart_summary(request)
    return render(request, 'ecart/cart.html', data)

from django.contrib import messages
from django.utils import timezone

def checkout_view(request):
    data = cart_summary(request)
    form = CheckoutForm()
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # form data
            full_name = form.cleaned_data['full_name']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']

            # cart total
            total = data['total']

            # create order (local store)
            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                total_amount=total,
                payment_status='Pending',
                created_at=timezone.now()
            )

            # save local details (optional)
            request.session['last_order'] = {
                'id': order.id,
                'name': full_name,
                'phone': phone,
                'address': address,
                'total': float(total),
            }

            # clear cart session
            request.session['cart'] = {}
            request.session.modified = True

            messages.success(request, 'Order placed successfully!')
            return redirect('ecart:payment_page')

    return render(request, 'ecart/checkout.html', {'form': form, 'data': data})


def order_summary_view(request):
    order_data = request.session.get('last_order')
    return render(request, 'ecart/order_summary.html', {'order': order_data})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ecart:profile')
    else:
        form = RegisterForm()
    return render(request, 'ecart/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('ecart:profile')
    else:
        form = AuthenticationForm()
    return render(request, 'ecart/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('ecart:home')


@login_required
def profile_view(request):
    orders = request.user.order_set.all()
    return render(request, 'ecart/profile.html', {'orders': orders})


def payment_page_view(request):
    order_data = request.session.get('last_order')
    if not order_data:
        return redirect('ecart:home')
    return render(request, 'ecart/payment_page.html', {'order': order_data})

@csrf_exempt
def payment_success_view(request):
    order_data = request.session.get('last_order')
    if order_data:
        order_id = order_data['id']
        from .models import Order
        order = Order.objects.filter(id=order_id).first()
        if order:
            order.payment_status = 'Paid'
            order.payment_id = f"PAY{order.id:04d}"
            order.save()
        request.session['last_order']['payment_status'] = 'Paid'
    return render(request, 'ecart/payment_success.html', {'order': order_data})

@csrf_exempt
def payment_cancel_view(request):
    order_data = request.session.get('last_order')
    if order_data:
        order_id = order_data['id']
        from .models import Order
        order = Order.objects.filter(id=order_id).first()
        if order:
            order.payment_status = 'Cancelled'
            order.save()
        request.session['last_order']['payment_status'] = 'Cancelled'
    return render(request, 'ecart/payment_cancel.html', {'order': order_data})

from django.db.models import Q

def search_products(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query),
            is_active=True
        )
    return render(request, 'ecart/search_results.html', {'query': query, 'results': results})

def home(request):
    category_slug = request.GET.get('category')
    products = Product.objects.filter(is_active=True)
    if category_slug:
        products = products.filter(category__slug=category_slug)
    categories = Category.objects.all()
    return render(request, 'ecart/home.html', {'products': products, 'categories': categories})





