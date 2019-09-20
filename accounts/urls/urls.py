from django.urls import path

from accounts.views.login import SystemUserLoginView, SystemUserLogoutView

__author__ = "Shafikur Rahman"

app_name = 'accounts'
urlpatterns = [
    path('login/', SystemUserLoginView.as_view(), name='login'),
    path('logout/', SystemUserLogoutView.as_view(), name='logout')
]
