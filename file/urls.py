from django.urls import path
from . import views

app_name="file"

urlpatterns = [
    path("get/<int:pk>/",views.stream_file,name="get_file"),
]
