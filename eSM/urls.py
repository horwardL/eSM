from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include(('catalogueApp.urls', 'catalogueApp'), "catalogueAppurls")),
    path('cart/', include(('cartApp.urls', 'cartApp'), "cartAppurls")),
    
    path('admin/', admin.site.urls),
]
