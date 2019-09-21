import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from meals.forms.meal import MealForm
from meals.models.meal import Meal


class MealCreateView(LoginRequiredMixin, CreateView):
    template_name = 'meals/add.html'
    form_class = MealForm

    def get_context_data(self, **kwargs):
        context = super(MealCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Meal - Create'
        context['page_headline'] = 'Meal(s)'
        return context

    def get(self, request, *args, **kwargs):
        return super(MealCreateView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        meal = form.save(commit=False)
        meal.add_by = self.request.user
        meal.save()
        meal_pk = str(meal.pk).zfill(4)
        meal.code = 'M-{0}'.format(meal_pk)
        meal.save()
        messages.success(self.request, 'Meal added successfully.')
        return HttpResponseRedirect(reverse('meals:meal-list'))


class MealListView(LoginRequiredMixin, ListView):
    template_name = 'meals/list.html'
    model = Meal
    paginate_by = 10
    context_object_name = 'objects_list'

    def get_context_data(self, **kwargs):
        context = super(MealListView, self).get_context_data(**kwargs)
        context['title'] = 'Meal - List'
        context['page_headline'] = 'Meal(s)'
        context['total_count'] = self.get_queryset().count()
        return context

    def get_queryset(self):
        object_list = super(MealListView, self).get_queryset()
        search = self.request.GET.get('search1', None)

        current_month = datetime.datetime.now().month
        object_list = object_list.filter(
            is_delete=False,
            member_id=self.request.user.pk,
            meal_date__month=current_month
        )
        if search:
            object_list = object_list.filter(name__icontains=search)
        return object_list.values(
            'pk', 'code', 'uuid', 'member__username', 'meal_date', 'breakfast', 'lunch', 'dinner', 'add_by__username',
            'is_delete',
            'add_at', 'change_at'
        ).order_by('-pk')


class MealChangeView(LoginRequiredMixin, UpdateView):
    template_name = 'meals/change.html'
    model = Meal
    form_class = MealForm
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_context_data(self, **kwargs):
        context = super(MealChangeView, self).get_context_data(**kwargs)
        context['title'] = 'Member - Update'
        context['page_headline'] = context['object'].meal_date
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.change_by = self.request.user
        user.save()
        messages.success(self.request, 'Meal updated successfully.')
        return HttpResponseRedirect(reverse('meals:meal-list'))


class MealDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'meals/delete.html'
    model = Meal
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_context_data(self, **kwargs):
        context = super(MealDelete, self).get_context_data(**kwargs)
        context['title'] = 'Meal - Delete'
        context['page_headline'] = context['object'].meal_date
        return context

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse('meals:meal-list'))
        else:
            user = self.get_object()
            user.delete_by = self.request.user
            user.delete_at = timezone.now()
            user.is_delete = True
            user.save()
            messages.error(self.request, 'Meal deleted successfully.')
            return HttpResponseRedirect(reverse('meals:meal-list'))


class MealDetailView(LoginRequiredMixin, DetailView):
    template_name = 'meals/detail.html'
    model = Meal
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_context_data(self, **kwargs):
        context = super(MealDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Meal - Details'
        context['page_headline'] = context['object'].username
        return context

    def get_queryset(self):
        queryset = super(MealDetailView, self).get_queryset()
        return queryset.select_related('add_by', 'change_by')
