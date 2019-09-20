from django.views.generic import TemplateView


class TemplateViewMixin(TemplateView):
    """
    Render a template. Pass keyword arguments from the URLconf to the context.
    """

    def get(self, request, *args, **kwargs):
        context = super(TemplateViewMixin, self).get_context_data(**kwargs)
        return self.render_to_response(context)
