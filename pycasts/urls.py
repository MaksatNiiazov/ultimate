from django.urls import path

from pycasts.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
]