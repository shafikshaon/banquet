from django.views.generic import ListView

__author__ = "Shafikur Rahman"


class ListViewMixin(ListView):
    """
    Override ListView class
    """
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListViewMixin, self).get_context_data(object_list=None, **kwargs)
        context['order_by_columns'] = self.model.get_order_by_columns
        context['searchable_columns'] = self.model.get_searchable_columns
        context['search_keyword'] = self.request.GET.get('search', None)
        context['title'] = ''
        context['page_headline'] = ''
        return context
