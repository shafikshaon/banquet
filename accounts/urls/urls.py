from django.urls import path

from accounts.views import SystemUserListView
from accounts.views.login import SystemUserLoginView, SystemUserLogoutView
from accounts.views.system_user import SystemUserAddView

__author__ = "Shafikur Rahman"

app_name = 'accounts'
urlpatterns = [
    path('login/', SystemUserLoginView.as_view(), name='login'),
    path('logout/', SystemUserLogoutView.as_view(), name='logout'),
    path('members/', SystemUserListView.as_view(), name='member-list'),
    path('members/add/', SystemUserAddView.as_view(), name='member-add'),
]
