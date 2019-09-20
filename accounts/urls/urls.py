from django.contrib.auth.views import LoginView
from django.urls import path

from accounts.views.login import SystemUserLoginView

__author__ = "Shafikur Rahman"

app_label = 'accounts'
urlpatterns = [
    path('login/', SystemUserLoginView.as_view(), name='login')
]
