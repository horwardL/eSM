from django.urls import path
from cartApp import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
]
