from django.urls import path
from client.views import ClientInformationView
app_name='client'
urlpatterns = [
    path("information/",ClientInformationView.as_view(),name="client-information")
]
