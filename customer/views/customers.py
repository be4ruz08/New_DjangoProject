import csv
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.core.mail import send_mail
from customer.forms import CustomerModelForm, AuthenticationForm
from customer.models import Customer, Order
import json
import openpyxl
from django.db.models import Avg, Count, Max, Min, Sum, F


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


def send_email_view(request):
    sent = False
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, 'bexruzbxdrv@gmail.com', [recipient])
            return HttpResponse('Email sent successfully')
    else:
        form = AuthenticationForm()
    return render(request, 'email/verify_email_confirm.html', {'form': form})


def order_statistics_view(request):
    total_orders = Order.objects.aggregate(total=Count('id'))
    total_order_value = Order.objects.aggregate(total_value=Sum(F('price') * F('quantity')))
    average_order_price = Order.objects.aggregate(average_price=Avg(F('price') * F('quantity')))
    max_order_price = Order.objects.aggregate(max_price=Max(F('price') * F('quantity')))
    min_order_price = Order.objects.aggregate(min_price=Min(F('price') * F('quantity')))

    context = {
        'total_orders': total_orders['total'],
        'total_order_value': total_order_value['total_value'],
        'average_order_price': average_order_price['average_price'],
        'max_order_price': max_order_price['max_price'],
        'min_order_price': min_order_price['min_price'],
    }
    return render(request, 'customer/order_statistics.html', context)


def customer_annotations_view(request):
    customers_with_order_count = Customer.objects.annotate(order_count=Count('order'))
    customers_with_total_order_value = Customer.objects.annotate(total_order_value=Sum(F('order__price') * F('order__quantity')))

    context = {
        'customers_with_order_count': customers_with_order_count,
        'customers_with_total_order_value': customers_with_total_order_value,
    }
    return render(request, 'customer/customer_annotations.html', context)