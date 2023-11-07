
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products", views.fetchProducts, name="product"),
    path("login",views.loginuser,name="login"),
    path("logout",views.logoutuser,name="logout"),
    path("sell",views.sell,name="sell"),
    path("saveproduct",views.saveProduct,name="saveproduct"),
]
