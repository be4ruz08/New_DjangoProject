from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from customer.forms import LoginForm, RegisterModelForm, EmailForm
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
from django.http import HttpResponse


# def login_page(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('customers')
#     else:
#         form = LoginForm()
#
#     return render(request, 'auth/login.html', {'form': form})

class LoginPageView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('customers')


def logout_page(request):
    if request.method == 'GET   ':
        logout(request)
        return redirect('customers')
    return render(request, 'auth/logout.html')


# permission = 'customer.add_customer'
# @permission_required(permission,'/login/',raise_exception=True)
# def register_page(request):
#     if request.method == 'POST':
#         form = RegisterModelForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             password = form.cleaned_data['password']
#
#             user.set_password(password)
#             user.save()
#
#             login(request, user)
#             return redirect('customers')
#     else:
#         form = RegisterModelForm()
#
#     return render(request, 'auth/register.html', {'form': form})

class RegisterView(CreateView):
    template_name = 'auth/register.html'
    form_class = RegisterModelForm
    success_url = reverse_lazy('customers')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data['email']
        user.password = form.cleaned_data['password']
        user.save()
        login(self.request, user)
        return redirect('customers')


def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, 'your_email@example.com', [recipient])
            return HttpResponse('Email sent successfully')
    else:
        form = EmailForm()
    return render(request, 'send_email.html', {'form': form})