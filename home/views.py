from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from home.models import Product
# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"index.html")

def product(request):
    return render(request,"products.html")

def sell(request):
    return render(request,"sell.html")

def saveProduct(request):
    if request.method=="POST":
        title=request.POST.get('Title')
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        img=request.POST.get('image')
        print(title,desc,price)
        en=Product(title=title,description=desc,price=price,image=img)
        en.save()
    return render(request,"sell.html")

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request,"login.html")
    return render(request,"login.html")

def logoutuser(request):
    logout(request)
    return redirect("/login")

def fetchProducts(request):
    allProducts=Product.objects.all()
    context={"products":allProducts}
    return render(request,"products.html",context)