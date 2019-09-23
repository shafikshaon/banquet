from configuration.views.meal_config import MealConfigListView, MealConfigAddView, MealConfigChangeView, \
    MealConfigDelete, MealConfigDetailView

__author__ = "Shafikur Rahman"
from django.urls import path
app_name='configuration'
urlpatterns = [
    path('meal-configs/', MealConfigListView.as_view(), name='meal-config-list'),
    path('meal-configs/add/', MealConfigAddView.as_view(), name='meal-config-add'),
    path('meal-configs/update/<uuid>/', MealConfigChangeView.as_view(), name='meal-config-change'),
    path('meal-configs/delete/<uuid>/', MealConfigDelete.as_view(), name='meal-config-delete'),
    path('meal-configs/detail/<uuid>/', MealConfigDetailView.as_view(), name='meal-config-detail'),
]
