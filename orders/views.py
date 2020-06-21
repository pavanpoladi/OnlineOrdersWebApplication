from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import json

from .models import Food

#Creating cart to hold all the food the user added to their cart
cart = []
totalPrice = [0.00]

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    context = {
        "user": request.user,
        "options": Food.objects.all()
    }
    return render(request, "orders/index.html", context)


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    email = request.POST.get('email')
    user = authenticate(request, username=username, password=password, firstName=firstName, lastName=lastName, email=email)
    if user is not None:
        #if user is an admin send them to the orders/checkout page
        if username == "pavan" and password == "pavan12345":
            login(request, user)
            context = {
                "user": request.user,
                "cart": cart,
                "totalPrice": totalPrice[0],
            }
            return render(request, "orders/checkout.html", context)
        else:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})


def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})


def getCart_view(request):
    listOfCartItems = json.dumps(cart)
    return HttpResponse(listOfCartItems)


def getTotal_view(request):
    return HttpResponse(totalPrice[0])


def updateTotal_view(request):
    newTotal = request.POST["totalPrice"]
    newTotal = json.loads(newTotal)
    totalPrice[0] = newTotal
    return HttpResponse("success")


def addToCart_view(request):
    listOfCartItems = request.POST["currentCart"]
    listOfCartItems = json.loads(listOfCartItems)
    cart.append(listOfCartItems[-1])
    listOfCartItems = json.dumps(cart)
    return HttpResponse(listOfCartItems)


def emptyCartAndTotalPrice_view(request):
    cart.clear()
    cart.append("Your order has been approved! Your food should be ready to pick up in approximately 15 minutes!")
    totalPrice[0] = 0.00
    return HttpResponse("success")


def checkout_view(request):
    context = {
        "user": request.user,
        "options": Food.objects.all(),
        "listOfCartItems": cart
    }
    return render(request, "orders/index.html", context)

