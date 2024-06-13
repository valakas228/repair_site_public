from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment, Cart, CartItem, PriceList, RepairService, City, Order, OrderItem, RepairRequest
from .forms import EstimateForm, OrderForm, CreateRepairRequestForm
from django.contrib.auth.decorators import login_required, user_passes_test


def store(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    products = Product.objects.all()
    return render(request, 'store/product_list.html',
                  {'products': products, 'cart_items': cart_items, 'total_price': total_price, })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'store/product_detail.html',
                  {'product': product, 'cart_items': cart_items, 'total_price': total_price})



@login_required
def add_comment(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            author = request.user
            comment = Comment.objects.create(text=comment_text, product=product, author=author)
    return redirect('product_detail', slug=product.slug)


@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'store/cart_items.html',
                  {'cart': cart, 'cart_items': cart_items, 'total_price': total_price})


def price_list(request):
    price_list = PriceList.objects.all()
    return render(request, 'store/price_list.html', {'price_list': price_list})


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


def estimate_cost(request):
    if request.method == 'POST':
        device_id = request.POST.get('device')
        issue_id = request.POST.get('issue')
        city_id = request.POST.get('city')

        device = Product.objects.get(id=device_id)
        issue = RepairService.objects.get(id=issue_id)
        city = City.objects.get(id=city_id)

        estimated_cost = calculate_cost(device, issue, city)

        context = {
            'device': device,
            'issue': issue,
            'city': city,
            'estimated_cost': estimated_cost,
        }
        return render(request, 'store/form_result.html', context)
    else:
        products = Product.objects.all()
        cities = City.objects.all()
        return render(request, 'store/estimate_form.html', {'products': products, 'cities': cities})


def get_issues(request):
    product_id = request.GET.get('product_id')
    issues = RepairService.objects.filter(device_id=product_id).values('id', 'service_name')
    return JsonResponse(list(issues), safe=False)


def calculate_cost(device, issue, city):
    base_cost = issue.price

    if city.name.lower() == "москва":
        base_cost += 200
    elif city.name.lower() == "спб":
        base_cost += 150
    elif city.name.lower() == "новосибирск":
        base_cost += 100

    if device.category.name.lower() == "смартфон" and issue.service_name.lower() == "экран":
        base_cost += 50

    return base_cost


def create_order(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            user = request.user
            order, created = Order.objects.get_or_create(user=user)
            order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
            order_item.quantity += quantity
            order_item.save()
            return redirect('view_cart')
    else:
        form = OrderForm()
    return render(request, 'store/create_order.html', {'form': form, 'product': product})

@login_required
def create_repair_request(request):
    if request.method == 'POST':
        form = CreateRepairRequestForm(request.POST)
        if form.is_valid():
            repair_request = form.save(commit=False)
            repair_request.user = request.user
            repair_request.save()
            return redirect('repair_request_success')
    else:
        form = CreateRepairRequestForm()
    return render(request, 'store/create_repair_request.html', {'form': form})

@login_required
def repair_request_success(request):
    return render(request, 'store/repair_request_success.html')

def is_admin(user):
    return user.is_staff