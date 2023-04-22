from django.shortcuts import render


def main(request):
    return render(request,
                  'main/pages/main.html',
                  context={
                      'main': 'ISTO É UM TESTE.'
                  },
                  )
