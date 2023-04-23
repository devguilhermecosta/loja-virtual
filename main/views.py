from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse, Http404
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
    send_message_data = request.session.get('send_message_contact', None)

    contact_form: Form = ContactUsForm(send_message_data)

    return render(
        request,
        'main/pages/contact_us.html',
        context={
            'form': contact_form,
        }
    )


def send_message(request: HttpRequest) -> HttpResponse:
    if not request.POST:
        raise Http404()

    post: dict = request.POST
    request.session['send_message_contact'] = post
    contact_form: Form = ContactUsForm(data=post)

    if contact_form.is_valid():
        print('mensagem enviada')
        del request.session['send_message_contact']
        return redirect(reverse('main:contact'))

    print('mensagem não enviada')
    return redirect(reverse('main:contact'))
