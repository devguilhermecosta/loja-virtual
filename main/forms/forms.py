from django import forms
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
import os


class ContactUsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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

    def send_message_from_email(self) -> None:
        message: str = (
            f'Nome: {self.data["name"]} \n'
            f'Email: {self.data["email"]} \n'
            f'Mensagem: {self.data["message"]}'
        )

        send_mail(
            f'{self.cleaned_data.get("name")}',
            message,
            self.data['email'],
            [os.environ.get('EMAIL_HOST_USER')],
            fail_silently=False
        )

    def clean_name(self) -> str:
        name_field = self.cleaned_data.get('name', '')

        if len(name_field) < 5:
            raise ValidationError(
                'O campo precisa ter pelo menos 5 caracteres'
                )

        return name_field

    def clean_message(self) -> str:
        message_field = self.cleaned_data.get('message', '')

        if len(message_field) < 5:
            raise ValidationError(
                'O campo precisa ter pelo menos 5 caracteres'
                )

        return message_field
