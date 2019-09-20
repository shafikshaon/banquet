from django.urls import path

from gist.views import DashboardView

__author__ = 'Shafikur Rahman'

app_name = 'gist'
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard')
]
