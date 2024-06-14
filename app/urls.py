from django.contrib import admin
from django.urls import path, include
from app.views import index, product_detail, add_product
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('product-detail/<int:product_id>', product_detail, name='product_detail'),
    path('add-product/', add_product, name='add_product'),
    path('customers/', views.customers, name='customers'),
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('add-customer/', views.add_customer, name='add_customer'),
]
