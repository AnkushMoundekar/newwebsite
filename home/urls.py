
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products", views.product, name="product"),
    path("login",views.loginuser,name="login"),
    path("logout",views.logoutuser,name="logout"),
]
