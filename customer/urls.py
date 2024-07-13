from django.urls import path

from customer.views.auth import login_page, logout_page, register_page
from customer.views.customers import CustomerListTemplateView, AddCustomerTemplateView, DeleteCustomerTemplateView, EditCustomerTemplateView, ExportDataTemplateView

app_name = 'customer'

urlpatterns = [
    path('customer-list/', CustomerListTemplateView.as_view(), name='customers'),
    path('add-customer/', AddCustomerTemplateView.as_view(), name='add_customer'),
    path('customer/<int:pk>/delete', DeleteCustomerTemplateView.as_view(), name='delete'),
    path('customer/<int:pk>/update', EditCustomerTemplateView.as_view(), name='edit'),
    # Authentication path
    path('login-page/', login_page, name='login'),
    path('logout-page/', logout_page, name='logout'),
    path('register-page/', register_page, name='register'),
    path('export-data/', ExportDataTemplateView.as_view(), name='export_data')
]