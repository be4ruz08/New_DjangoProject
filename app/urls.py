from django.contrib import admin
from django.urls import path, include
from app.views import index, product_detail, add_product
from app import views
from customer.views import customers, add_customer, delete_customer, edit_customer
from login.views import login_view, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('product-detail/<int:product_id>', product_detail, name='product_detail'),
    path('add-product/', add_product, name='add_product'),
    path('customer-list/', customers, name='customers'),
    path('add-customer/', add_customer, name='add_customer'),
    path('customer/<int:pk>/delete', delete_customer, name='delete'),
    path('customer/<int:pk>/update', edit_customer, name='edit'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
