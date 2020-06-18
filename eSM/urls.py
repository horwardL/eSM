from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include(('catalogueApp.urls', 'catalogueApp'), "catalogueUrls")),
    path('', include(('cartApp.urls', 'cartApp'), "cartUrls")),
    
    path('admin/', admin.site.urls),
]
