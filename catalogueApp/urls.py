from django.urls import path
from catalogueApp import views

urlpatterns = [
    path('', views.catalogue, name='catalogue'),
    path('catalogue/<category_slug>/<market_slug>/', views.catalogue, name='catalogue'),
    path('catalogue/products/<product_slug>/', views.product_detail, name='product_detail'),
]
