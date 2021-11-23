from django.urls import path
from . import views
app_name='vendor'
urlpatterns = [
    path("become-a-vendor/",views.CreateVendorView.as_view(),name='become-a-vendor'),
    path("dashboard/",views.VendorDashboard.as_view(),name='dashboard'),
]
