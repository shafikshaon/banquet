from django.views.generic import TemplateView

__author__ = 'Shafikur Rahman'


class DashboardView(TemplateView):
    template_name = 'gist/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context
