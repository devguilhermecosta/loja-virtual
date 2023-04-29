from django.urls import path
from . import views


app_name: str = 'cart'

urlpatterns: list = [
    path('', views.cart_details, name='details'),
    path('add/<int:id>/', views.add_to_cart, name='add'),
    path('remove/<int:id>/', views.remove_to_cart, name='remove'),
]
