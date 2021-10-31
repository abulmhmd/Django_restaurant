from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="Store"),
    path('contact_us/', views.contact, name="contact_us"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('customer_form/', views.customerFeed, name="customer_form"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    

]
