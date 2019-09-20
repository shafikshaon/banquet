from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import resolve_url

from accounts.forms.login import LoginForm

__author__ = 'Shafikur Rahman'


class SystemUserLoginView(LoginView):
    template_name = "accounts/login.html"
    form_class = LoginForm

    def get_success_url(self):
        return resolve_url(settings.LOGIN_REDIRECT_URL)


class SystemUserLogoutView(LogoutView):
    template_name = "accounts/logout.html"
