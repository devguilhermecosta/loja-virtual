from django.http import HttpRequest
from django.conf import settings
from main.models import Product
from typing import Optional
from decimal import Decimal


class Cart:
    def __init__(self, request: HttpRequest) -> None:
        self.__session = request.session
        self.__cart: dict = self.__session.get(settings.CART_ID)
        if not self.__cart:
            self.__cart = self.__session[settings.CART_ID] = {}

    def add_product(self,
                    product: Product,
                    quantity: int,
                    update_quantity: Optional[bool] = False) -> None:
        id_product: str = str(product.id)
        if id_product not in self.__cart:
            self.__cart[id_product] = {
                'quantity': 0,
                'price': str(product.price)
            }

        if update_quantity:
            self.__cart['id_product']['quantity'] = quantity

        else:
            self.__cart['id_product']['quantity'] += quantity

        self.__save()

    def __save(self) -> None:
        self.__session[settings.CART_ID] = self.__cart
        self.__session.modified = True

    def remove(self, product: Product) -> None:
        product_id: str = str(product.id)
        if product_id in self.__cart:
            del self.__cart[product_id]
            self.__save()

    def __iter__(self):
        products_ids = self.__cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        cart = self.__cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product
            for item in cart.values():
                item['price'] = Decimal(item['price'])
                item['subtotal'] = (
                    Decimal(item['price']) * Decimal(item['quantity'])
                    )
                yield item

    def __len__(self) -> int:
        result: int = 0
        for item in self.__cart.values():
            result += item['quantity']
        return result

    def get_total(self) -> Decimal:
        result: Decimal = Decimal(0.0)
        for item in self.__cart.values():
            subtotal = Decimal(item['quantity']) * Decimal(item['price'])
            result += subtotal
        return result

    def clean_cart(self) -> None:
        for key in self.__session.keys():
            del self.__session.keys[key]
        self.__session.modified = True
