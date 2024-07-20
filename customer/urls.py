from django.urls import path

from customer.views.auth import login_page, logout_page, register_page, LoginPageView, LoginPage, RegisterFormView, \
    verify_email_confirm, verify_email_done
from customer.views.customers import CustomerListTemplateView, AddCustomerTemplateView, DeleteCustomerTemplateView, EditCustomerTemplateView, ExportDataTemplateView, send_email_view

urlpatterns = [
    path('customer-list/', CustomerListTemplateView.as_view(), name='customers'),
    path('add-customer/', AddCustomerTemplateView.as_view(), name='add_customer'),
    path('customer/<int:pk>/delete', DeleteCustomerTemplateView.as_view(), name='delete'),
    path('customer/<int:pk>/update', EditCustomerTemplateView.as_view(), name='edit'),
    # Authentication path
    path('login-page/', LoginPage.as_view(), name='login'),
    path('logout-page/', logout_page, name='logout'),
    path('register-page/', register_page, name='register'),
    path('export-data/', ExportDataTemplateView.as_view(), name='export_data'),
    path('sending-mail/', send_email_view(), name='share_mail'),
    # sending
    path('verify-email-done/', verify_email_done, name='verify_email_done'),
    path('verify-email-confirm/<uidb64>/<token>/', verify_email_confirm, name='verify_email_confirm'),
]