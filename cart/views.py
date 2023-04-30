from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import FormAddProductToCart
from main.models import Product


@require_POST
def add_to_cart(request: HttpRequest, product_id: int) -> HttpResponse:
    cart = Cart(request)
    product = get_object_or_404(Product,
                                id=product_id,
                                )
    form = FormAddProductToCart(request.POST)

    if form.is_valid():
        data = form.cleaned_data
        cart.add_product(product=product,
                         quantity=data['quantity'],
                         update_quantity=data['update'],
                         )
        return redirect('cart:details')


def remove_to_cart(request: HttpRequest, product_id: int) -> HttpResponse:
    cart = Cart(request)
    product = get_object_or_404(Product,
                                id=product_id,
                                )
    cart.remove(product)
    return redirect('cart:details')


def cart_details(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)
    for item in cart:
        item['form_add_to_cart'] = FormAddProductToCart(
            initial={
                'quantity': item['quantity'],
                'update': True
            }
        )
    return render(
        request,
        'cart/pages/details.html',
        context={
            'cart': cart,
        }
    )
