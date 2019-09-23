from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from configuration.forms.meal_config import MealConfigForm
from configuration.models import MealConfig
from gist.mixins.ListViewMixin import ListViewMixin


class MealConfigListView(LoginRequiredMixin, ListViewMixin):
    template_name = 'configuration/meal_config/list.html'
    model = MealConfig
    paginate_by = 10
    context_object_name = 'objects_list'

    def get_context_data(self, **kwargs):
        context = super(MealConfigListView, self).get_context_data(**kwargs)
        context['title'] = 'Meal Config - List'
        context['page_headline'] = 'Meal Config(s)'
        context['total_count'] = self.get_queryset().count()
        return context

    def get_queryset(self):
        object_list = super(MealConfigListView, self).get_queryset()
        search = self.request.GET.get('search1', None)
        if search:
            object_list = object_list.filter(name__icontains=search)
        return object_list.filter(is_delete=False).values(
            'pk', 'code', 'uuid', 'breakfast', 'lunch', 'dinner', 'add_by__username', 'is_delete',
            'add_at', 'change_at'
        ).order_by('-pk')


class MealConfigAddView(LoginRequiredMixin, CreateView):
    template_name = 'configuration/meal_config/add.html'
    form_class = MealConfigForm

    def get_context_data(self, **kwargs):
        context = super(MealConfigAddView, self).get_context_data(**kwargs)
        context['title'] = 'Meal Config - Create'
        context['page_headline'] = 'Meal Config(s)'
        return context

    def get(self, request, *args, **kwargs):
        return super(MealConfigAddView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        meal_config = form.save(commit=False)
        meal_config.add_by = self.request.user
        meal_config.save()
        meal_config_pk = str(meal_config.pk).zfill(4)
        meal_config.code = 'MC-{0}'.format(meal_config_pk)
        meal_config.save()
        messages.success(self.request, 'Meal Config added successfully.')
        return HttpResponseRedirect(reverse('configuration:meal-config-list'))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class MealConfigChangeView(LoginRequiredMixin, UpdateView):
    template_name = 'configuration/meal_config/change.html'
    model = MealConfig
    form_class = MealConfigForm
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_context_data(self, **kwargs):
        context = super(MealConfigChangeView, self).get_context_data(**kwargs)
        context['title'] = 'Meal Config - Update'
        context['page_headline'] = context['object'].code
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.change_by = self.request.user
        user.save()
        messages.success(self.request, 'Meal Config updated successfully.')
        return HttpResponseRedirect(reverse('configuration:meal-config-list'))


class MealConfigDelete(LoginRequiredMixin, DeleteView):
    template_name = 'configuration/meal_config/delete.html'
    model = MealConfig
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_context_data(self, **kwargs):
        context = super(MealConfigDelete, self).get_context_data(**kwargs)
        context['title'] = 'Meal Config - Delete'
        context['page_headline'] = context['object'].code
        return context

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse('configuration:meal-config-list'))
        else:
            user = self.get_object()
            user.delete_by = self.request.user
            user.delete_at = timezone.now()
            user.is_delete = True
            user.save()
            messages.error(self.request, 'Meal Config deleted successfully.')
            return HttpResponseRedirect(reverse('configuration:meal-config-list'))


class MealConfigDetailView(LoginRequiredMixin, DetailView):
    template_name = 'configuration/meal_config/detail.html'
    model = MealConfig
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_context_data(self, **kwargs):
        context = super(MealConfigDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Meal Config - Details'
        context['page_headline'] = context['object'].code
        return context

    def get_queryset(self):
        queryset = super(MealConfigDetailView, self).get_queryset()
        return queryset.select_related('add_by', 'change_by')
