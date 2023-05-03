from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from cart.cart import Cart
from .models import OrderItem
from .forms import CreateOrderForm


def create_order(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                )
            cart.clean_cart()
            return render(
                request,
                'orders/pages/create.html',
                context={
                    'order': order,
                }
            )
    else:
        form = CreateOrderForm()
    return render(
        request,
        'orders/pages/create.html',
        context={
            'cart': cart,
            'form': form,
        }
    )
