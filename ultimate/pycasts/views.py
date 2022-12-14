from django.views.generic import ListView

from pycasts.models import Episode


class HomePageView(ListView):
    template_name = "homepage.html"
    model = Episode
    context_object_name = "episodes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["episodes"] = Episode.objects.filter().order_by("-pub_date")[:10]
        return context