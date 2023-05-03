from django.db import models
from decimal import Decimal
from main.models import Product


class Order(models.Model):
    # person data
    name = models.CharField(max_length=50)
    email = models.EmailField()
    adress = models.CharField(max_length=50)
    number = models.CharField(max_length=5)
    neighborhood = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    complement = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    postal = models.CharField(max_length=9)

    # order data
    created_at = models.DateField(auto_now=True)
    paid_out = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'Order: {self.id}'

    def get_total_price(self) -> Decimal:
        result: Decimal = Decimal(0.0)
        for item in self.itens.all():
            subtotal = Decimal(
                Decimal(item['price']) * Decimal(item['quantity'])
                )
            result += subtotal
        return result


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='itens',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_itens',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f'Order: {self.id}'

    def get_subtotal(self) -> float | int:
        return self.price * self.quantity
