from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


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
