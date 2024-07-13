from django.contrib import admin
from django.urls import path
from app.views import ProductListView, ProductDetailTemplateView, AddProductView, EditProductTemplateView, ProductDeleteView
from customer.views.auth import login_page, logout_page, register_page
from customer.views.customers import CustomerListTemplateView, AddCustomerTemplateView, DeleteCustomerTemplateView, EditCustomerTemplateView, ExportDataTemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', ProductListView.as_view(), name='index'),
    path('product-detail/<int:product_id>', ProductDetailTemplateView.as_view(), name='product_detail'),
    path('add-product/', AddProductView.as_view(), name='add_product'),
    path('edit-product/<int:product_id>', EditProductTemplateView.as_view(), name='edit_product'),
    path('delete-product/<int:product_id>', ProductDeleteView.as_view(), name='delete_customer'),
    path('customer-list/', CustomerListTemplateView.as_view(), name='customers'),
    path('add-customer/', AddCustomerTemplateView.as_view(), name='add_customer'),
    path('customer/<int:pk>/delete', DeleteCustomerTemplateView.as_view(), name='delete'),
    path('customer/<int:pk>/update', EditCustomerTemplateView.as_view(), name='edit'),
    path('export-data/', ExportDataTemplateView.as_view(), name='export_data'),
    path('login-page/', login_page, name='login'),
    path('logout-page/', logout_page, name='logout'),
    path('register-page', register_page, name='register'),
]
