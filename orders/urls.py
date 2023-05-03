from django.urls import path
from . import views

app_name: str = 'order'

urlpatterns: list = [
    path('create/', views.create_order, name='create'),
]
