from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include(('catalogueApp.urls', 'catalogueApp'), "catalogueUrls")),
    path('admin/', admin.site.urls),
]
