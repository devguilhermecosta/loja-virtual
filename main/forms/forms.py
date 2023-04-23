from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100,
                           required=True,
                           label='Seu nome',
                           widget=forms.TextInput(
                               attrs={
                                   'placeholder': 'Ex: João da Silva',
                                   'class': 'C-form__input',
                               }
                           )
                           )
    email = forms.EmailField(max_length=255,
                             required=True,
                             label='Email',
                             widget=forms.EmailInput(
                                 attrs={
                                     'placeholder': 'email@email.com',
                                     'class': 'C-form__input',
                                 }
                             )
                             )
    message = forms.CharField(max_length=255,
                              required=True,
                              label='Mensagem',
                              widget=forms.Textarea(
                                  attrs={
                                      'placeholder': 'Sua mensagem',
                                      'class': 'C-form__textarea',
                                  }
                              )
                              )
