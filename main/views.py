from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpRequest, HttpResponse, Http404
from django.forms import Form
from main.forms.forms import ContactUsForm
from main.models import Product, Category
from cart.forms import FormAddProductToCart


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
        contact_form.send_message_from_email()
        del request.session['send_message_contact']
        return redirect(reverse('main:contact'))

    return redirect(reverse('main:contact'))


def products_list(request: HttpRequest,
                  slug_category: str | None = None) -> HttpResponse:
    category: Category | None = None
    products: Product = Product.objects.filter(available=True)
    category_list: Category = Category.objects.all()

    if slug_category:
        category = get_object_or_404(Category,
                                     slug=slug_category,
                                     )
        products = Product.objects.filter(available=True,
                                          category=category,
                                          )

    return render(
        request,
        'main/pages/products_list.html',
        context={
            'products': products,
            'category_list': category_list,
            'category': category,
        }
    )


def product_detail(request: HttpRequest, id: int, slug: str) -> HttpResponse:
    product: Product = get_object_or_404(Product,
                                         id=id,
                                         slug=slug,
                                         available=True,
                                         )

    category_list: Category = Category.objects.all()

    add_product_form = FormAddProductToCart()

    return render(request,
                  'main/pages/product_detail.html',
                  context={
                      'product': product,
                      'category_list': category_list,
                      'add_product_form': add_product_form,
                  })
