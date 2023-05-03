from .models import Order
from django import forms


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name',
                  'email',
                  'adress',
                  'number',
                  'neighborhood',
                  'city',
                  'complement',
                  'state',
                  'postal']
