from django.conf import settings
from django.contrib.auth.views import LoginView
from django.shortcuts import resolve_url

from accounts.forms.login import LoginForm

__author__ = 'Shafikur Rahman'


class SystemUserLoginView(LoginView):
    template_name = "accounts/login.html"
    form_class = LoginForm
