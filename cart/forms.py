from django import forms

QUANTITY_PRODUCT: list = []

for i in range(1, 51):
    QUANTITY_PRODUCT.append((i, str(i)))


class FormAddProductToCart(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=QUANTITY_PRODUCT,
        coerce=int,
    )
    update = forms.BooleanField(required=False,
                                widget=forms.HiddenInput,
                                )
