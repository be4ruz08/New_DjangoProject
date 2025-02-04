from django.contrib import admin
from django.urls import path
from app.views import ProductListView, ProductDetailTemplateView, AddProductView, EditProductTemplateView, ProductDeleteView
from customer.views.auth import LoginPageView, logout_page, RegisterFormView, LoginPage, verify_email_done, \
    verify_email_confirm
from customer.views.customers import CustomerListTemplateView, AddCustomerTemplateView, DeleteCustomerTemplateView, \
    EditCustomerTemplateView, ExportDataTemplateView, send_email_view
from .views import product_statistics_view, product_annotations_view
from customer.views.customers import order_statistics_view, customer_annotations_view

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
    path('login-page/', LoginPage.as_view(), name='login'),
    path('logout-page/', logout_page, name='logout'),
    path('register-page', RegisterFormView.as_view(), name='register'),
    path('sending-mail/', send_email_view, name='share_mail'),
    path('verify-email-done/', verify_email_done, name='verify_email_done'),
    path('verify-email-confirm/<uidb64>/<token>/', verify_email_confirm, name='verify_email_confirm'),
    path('product-statistics/', product_statistics_view, name='product_statistics'),
    path('order-statistics/', order_statistics_view, name='order_statistics'),
    path('product-annotations/', product_annotations_view, name='product_annotations'),
    path('customer-annotations/', customer_annotations_view, name='customer_annotations'),
]
