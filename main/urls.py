from django.urls import path
from main import views

app_name: str = 'main'

urlpatterns: list = [
    path('', views.products_list, name='main'),
    path('ajuda/', views.help, name='help'),
    path('contato/', views.contact_us, name='contact'),
    path('contato/enviar-mensagem/', views.send_message, name='send_message'),
    path('produtos/', views.products_list, name='products_list'),
    path('produtos/<str:slug_category>/',
         views.products_list,
         name='products_list_filter'),
    path('produto/<int:id>/<str:slug>/',
         views.product_detail,
         name='product_detail'),
]
