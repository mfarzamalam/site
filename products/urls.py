from django.urls import path
from .views import show_product,show_product_on_sale
urlpatterns = [
    path("",show_product),
    path("onsale/",show_product_on_sale)
]