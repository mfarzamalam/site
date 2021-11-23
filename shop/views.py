from django.shortcuts import render

# Create your views here.
def show_shop_sidebar(request):
    return render(request, "shop/shop-sidebar.html")