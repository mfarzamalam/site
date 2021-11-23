
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("pages.urls")),
    path("product/",include("products.urls")),
    path("shop/",include("shop.urls")),
    path("registration/",include("registration.urls")),
    path("vendor/",include("vendor.urls")),
    path("file/",include("file.urls")),
    path("client/",include("client.urls")),
]
