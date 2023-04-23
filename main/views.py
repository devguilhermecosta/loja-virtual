from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.forms import Form
from main.forms.forms import ContactUsForm


def main(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'main/pages/main.html',
        )


def help(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        'main/pages/help.html',
    )


def contact_us(request: HttpRequest) -> HttpResponse:
    contact_form: Form = ContactUsForm()

    return render(
        request,
        'main/pages/contact_us.html',
        context={
            'form': contact_form,
        }
    )
