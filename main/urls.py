from django.urls import path
from .views import index
from .views import about

urlpatterns = [
    path("", about, name="about"),
    path("home/", index, name="index")
]
