from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100,
                           required=True,
                           )
    email = forms.EmailField(max_length=255,
                             required=True,
                             )
    message = forms.CharField(max_length=255,
                              required=True,
                              )
