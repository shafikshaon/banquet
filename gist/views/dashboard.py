from django.views.generic import TemplateView

from accounts.models import SystemUser

__author__ = 'Shafikur Rahman'


class DashboardView(TemplateView):
    template_name = 'gist/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['total_active_member'] = SystemUser.objects.filter(is_delete=False, is_active=True).count()
        return context
