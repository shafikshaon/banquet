from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import CreateView, UpdateView, DeleteView

from accounts.forms.system_user_change import SystemUserChangeForm
from accounts.forms.system_user_creation import SystemUserCreationForm
from accounts.models import SystemUser
from gist.mixins.ListViewMixin import ListViewMixin


class SystemUserListView(LoginRequiredMixin, ListViewMixin):
    template_name = 'accounts/list.html'
    model = SystemUser
    paginate_by = 10
    context_object_name = 'objects_list'

    def get_context_data(self, **kwargs):
        context = super(SystemUserListView, self).get_context_data(**kwargs)
        context['title'] = 'Member - List'
        context['page_headline'] = 'Member(s)'
        context['total_count'] = self.get_queryset().count()
        return context

    def get_queryset(self):
        object_list = super(SystemUserListView, self).get_queryset()
        search = self.request.GET.get('search1', None)
        if search:
            object_list = object_list.filter(name__icontains=search)
        return object_list.filter(is_delete=False).values(
            'pk', 'code', 'uuid', 'first_name', 'last_name', 'email', 'username', 'add_by__username', 'is_delete',
            'add_at', 'change_at'
        ).order_by('-pk')


class SystemUserAddView(LoginRequiredMixin, CreateView):
    template_name = 'accounts/add.html'
    form_class = SystemUserCreationForm

    def get_context_data(self, **kwargs):
        context = super(SystemUserAddView, self).get_context_data(**kwargs)
        context['title'] = 'Member - Create'
        context['page_headline'] = 'Member(s)'
        return context

    def get(self, request, *args, **kwargs):
        return super(SystemUserAddView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.add_by = self.request.user
        user.password1 = user.set_password(form.cleaned_data['password1'])
        user.save()
        user_pk = str(user.pk).zfill(4)
        user.code = 'SU-{0}'.format(user_pk)
        user.save()
        messages.success(self.request, 'Member added successfully.')
        return HttpResponseRedirect(reverse('accounts:members'))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class SystemUserChangeView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/change.html'
    model = SystemUser
    form_class = SystemUserChangeForm

    def get_context_data(self, **kwargs):
        context = super(SystemUserChangeView, self).get_context_data(**kwargs)
        context['title'] = 'Member - Update'
        context['page_headline'] = context['object'].username
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.change_by = self.request.user
        user.save()
        messages.success(self.request, 'Member updated successfully.')
        return HttpResponseRedirect(reverse('accounts:member-list'))


class SystemUserDelete(LoginRequiredMixin, DeleteView):
    template_name = 'accounts/delete.html'
    model = SystemUser

    def get_context_data(self, **kwargs):
        context = super(SystemUserDelete, self).get_context_data(**kwargs)
        context['title'] = 'Member - Delete'
        context['page_headline'] = context['object'].username
        return context

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse('accounts:member-list'))
        else:
            user = self.get_object()
            user.delete_by = self.request.user
            user.delete_at = timezone.now()
            user.is_delete = True
            user.save()
            messages.error(self.request, 'Member deleted successfully.')
            return HttpResponseRedirect(reverse('accounts:member-list'))
