from django.contrib import admin
from django.urls import path, include
from views import login_view, register_view, logout_view
from app.views import index, product_detail, add_product
from app import views
from customer.views import customers, add_customer, delete_customer, edit_customer

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

]
