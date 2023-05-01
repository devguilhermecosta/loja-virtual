from cart.cart import Cart
from django.http import HttpRequest


def cart(request: HttpRequest) -> dict:
    return {'cart': Cart(request)}
