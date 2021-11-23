from django.urls import path
from .views import show_shop_sidebar
urlpatterns = [
    path("",show_shop_sidebar)
]