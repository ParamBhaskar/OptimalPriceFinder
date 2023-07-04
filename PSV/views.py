from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from pr_com.models import Product, contacted_user

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

def contact(request):
    name=request.POST.get('FirstName')
    email=request.POST.get('Email')
    message= request.POST.get('textinput')
    # textinput=request.POST.get('textinput')
    # request.session['Email']= request.POST['Email']
    # subject = "Hello from "+ name + " having Email ID: "+ email + " via Contact Form of PSV"
    # email_from= email
    # email_to=["paramanandabhaskar@gmail.com"]
    # message= EmailMessage(subject, message,email_from,email_to)
    # message.send()
    user= contacted_user.objects.create(name=name, email=email, message=message)
    return redirect('/')
