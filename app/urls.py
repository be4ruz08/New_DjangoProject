from django.contrib import admin
from django.urls import path
from app.views import index, product_detail, add_product
from customer.views.auth import login_page, logout_page, register_page
from customer.views.customers import customers, add_customer, delete_customer, edit_customer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('product-detail/<int:product_id>', product_detail, name='product_detail'),
    path('add-product/', add_product, name='add_product'),
    path('customer-list/', customers, name='customers'),
    path('add-customer/', add_customer, name='add_customer'),
    path('customer/<int:pk>/delete', delete_customer, name='delete'),
    path('customer/<int:pk>/update', edit_customer, name='edit'),
    path('login-page/', login_page, name='login'),
    path('logout-page/', logout_page, name='logout'),
    path('register-page', register_page, name='register'),
]
