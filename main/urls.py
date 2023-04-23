from django.urls import path
from main import views

app_name: str = 'main'

urlpatterns: list = [
    path('', views.main, name='main'),
    path('ajuda/', views.help, name='help'),
]
