from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
def store(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products':products, 'cart_items':cart_items, 'total_price':total_price,})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_detail.html', {'product':product})

from .models import Product, Comment

def add_comment(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            comment = Comment.objects.create(text=comment_text, product=product)
    return redirect('product_detail', slug=product.slug)


def add_to_cart_ajax(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    total_items = cart.cartitem_set.count()
    return JsonResponse({'total_items': total_items})

def remove_from_cart_ajax(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    total_items = cart.cartitem_set.count()
    return JsonResponse({'total_items': total_items})

def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)

    cart = request.session.get('cart', [])
    cart.append(product.id)
    request.session['cart'] = cart

    return redirect('product_detail', slug=product.slug)

def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'store/cart_items.html', {'cart': cart, 'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('view_cart')