from django.urls import path
from . import views

urlpatterns = [
    path("crypto",views.home, name="home"),
    path("crypto/prices/", views.prices, name = "prices"),
]