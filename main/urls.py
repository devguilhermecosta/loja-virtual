from django.urls import path
from main import views

app_name: str = 'main'

urlpatterns: list = [
    path('', views.main, name='main'),
    path('ajuda/', views.help, name='help'),
    path('contato/', views.contact_us, name='contact'),
    path('contato/enviar-mensagem', views.send_message, name='send_message'),
]
