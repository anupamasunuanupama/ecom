from django.urls import path
from .import views

urlpatterns = [
    path("CartView",views.CartView,name="CartView"),
    path("AddCart/<int:pk>",views.AddCart,name="AddCart"),
    path("DeleteCart/<int:pk>",views.DeleteCart,name="DeleteCart"),
    path("Placeorder",views.Placeorder,name="Placeorder"),
    path("paymenthandler",views.paymenthandler,name="paymenthandler"),
    path("CustomerOrders",views.CustomerOrders,name="CustomerOrders"),
]
