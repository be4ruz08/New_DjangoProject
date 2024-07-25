from django.db.models.signals import post_save
from django.dispatch import receiver
from customer.models import User
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import FormView, CreateView
from customer.forms import LoginForm, RegisterModelForm
from django.contrib.auth.decorators import permission_required
from config import settings
from customer.models import User
from customer.views.tokens import account_activation_token


@receiver(post_save, sender=User)
def sending_links(sender, instance, created, **kwargs):
    if created:
        request = sender.request_class
        print('User Created')
        print(request)
    #     current_site = get_current_site(self.request)
    #
    #     subject = "Verify Email"
    #     message = render_to_string('email/verify_email_message.html', {
    #         'request': self.request,
    #         'user': user,
    #         'domain': current_site.domain,
    #         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    #         'token': account_activation_token.make_token(user),
    #     })
    #     email = EmailMessage(subject, message, to=[user.email])
    #     email.content_subtype = 'html'
    #
    #     email.send()
    # else:
    #     print('User Updated !')