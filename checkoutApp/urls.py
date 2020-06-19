from django.urls import path
from checkoutApp import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('receipt', views.receipt, name='receipt'),
]
