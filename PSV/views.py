from django.shortcuts import render
from django.http import HttpResponse
from pr_com.models import Product
def index(request):
    return render(request, 'index.html')
def food(request):
    return render(request, 'food.html')
def furniture(request):
    return render(request, 'furniture.html')
def clothes(request):
    return render(request, 'clothes.html')
def electronics(request):
    return render(request, 'electronics.html')

def my_view(request, stringextra):
    print(stringextra)
    return HttpResponse("Hello")


def view_cart(request):
    pros = Product.objects.all()
    return render(request, "productDisplay.html", {'pros': pros})
