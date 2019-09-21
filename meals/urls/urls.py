from meals.views.meal import MealCreateView, MealListView, MealChangeView, MealDetailView, MealDeleteView

__author__ = "Shafikur Rahman"
from django.urls import path

app_name = 'meals'
urlpatterns = [
    path('add/', MealCreateView.as_view(), name='meal-add'),
    path('list/', MealListView.as_view(), name='meal-list'),
    path('update/<uuid>/', MealChangeView.as_view(), name='meal-change'),
    path('detail/<uuid>/', MealDetailView.as_view(), name='meal-detail'),
    path('delete/<uuid>/', MealDeleteView.as_view(), name='meal-delete'),
]
