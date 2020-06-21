from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("getCart", views.getCart_view, name="getCart"),
    path("getTotal", views.getTotal_view, name="getTotal"),
    path("updateTotal", views.updateTotal_view, name="updateTotal"),
    path("addToCart", views.addToCart_view, name="addToCart"),
    path("checkout", views.checkout_view, name="checkout"),
    path("emptyCartAndTotalPrice", views.emptyCartAndTotalPrice_view, name="emptyCartAndTotalPrice")
]
