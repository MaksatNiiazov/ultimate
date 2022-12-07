from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from mydiary.models import Entry
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class LockedView(LoginRequiredMixin):
    login_url = "admin:login"


class EntryListView(LockedView, ListView):
    model = Entry
    template_name = "entries/entry_list.html"
    queryset = Entry.objects.all().order_by("-date_created")


class EntryDetail(LockedView, DetailView):
    template_name = "entries/entry_detail.html"
    model = Entry


class EntryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Entry
    template_name = "entries/entry_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")
    success_message = "Your new entry was created!"


class EntryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Entry
    template_name = "entries/entry_form.html"
    fields = ["title", "content"]
    success_message = "Your entry was updated!"

    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.object.pk}
        )


class EntryDeleteView(LockedView, DeleteView):
    model = Entry
    template_name = "entries/entry_confirm_delete.html"
    success_url = reverse_lazy("entry-list")
    success_message = "Your entry was deleted!"


