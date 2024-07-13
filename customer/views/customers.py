import csv
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from customer.forms import CustomerModelForm
from customer.models import Customer
import json
import openpyxl

# Create your views here.


class CustomerListTemplateView(TemplateView):
    template_name = 'customer/customer-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('search', '')
        if search_query:
            customer_list = Customer.objects.filter(
                Q(full_name__icontains=search_query) | Q(address__icontains=search_query))
        else:
            customer_list = Customer.objects.all()
        context['customer_list'] = customer_list
        return context


class AddCustomerTemplateView(TemplateView):
    template_name = 'customer/add-customer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CustomerModelForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CustomerModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customer-list')
        return self.render_to_response(self.get_context_data(form=form))


class DeleteCustomerTemplateView(TemplateView):
    def post(self, request, pk):
        customer = get_object_or_404(Customer, id=pk)
        customer.delete()
        messages.success(request, 'Customer successfully deleted')
        return redirect('customer-list')


class EditCustomerTemplateView(TemplateView):
    template_name = 'customer/update-customer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Customer.objects.get(id=kwargs['pk'])
        context['form'] = CustomerModelForm(instance=product)
        return context

    def post(self, request,  *args, **kwargs):
        context = self.get_context_data(**kwargs)

        customer = get_object_or_404(Customer, id=kwargs['pk'])
        form = CustomerModelForm(instance=customer, data=request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('customer-list')


class ExportDataTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        format = request.GET.get('format', 'csv')
        if format == 'csv':
            return self.export_csv()
        elif format == 'json':
            return self.export_json()
        elif format == 'xlsx':
            return self.export_xlsx()
        else:
            response = HttpResponse(status=404)
            response.content = 'Bad request'
            return response

    def export_csv(self):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=customers.csv'
        writer = csv.writer(response)
        writer.writerow(['Id', 'Full Name', 'Email', 'Phone Number', 'Address'])
        for customer in Customer.objects.all():
            writer.writerow([customer.id, customer.full_name, customer.email, customer.phone_number, customer.address])
        return response

    def export_json(self):
        response = HttpResponse(content_type='application/json')
        data = list(Customer.objects.all().values('full_name', 'email', 'phone_number', 'address'))
        response.write(json.dumps(data, indent=4))
        response['Content-Disposition'] = 'attachment; filename=customers.json'
        return response

    def export_xlsx(self):
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=customers.xlsx'
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['Id', 'Full Name', 'Email', 'Phone Number', 'Address'])
        customers = Customer.objects.all()
        for customer in customers:
            ws.append([customer.id, customer.full_name, customer.email, customer.phone_number, customer.address])
        wb.save(response)
        return response
