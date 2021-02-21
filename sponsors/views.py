from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect, HttpRequest
from .models import *
from django.views.generic import (TemplateView, ListView,
                                  CreateView, UpdateView,
                                  DetailView, DeleteView)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin                            

class ListSponsor(LoginRequiredMixin, ListView):
    template_name = 'sponsors/sponsor_dashboard.html'
    model = Sponsor
    context_object_name = 'sponsors'


class AddSponsor(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'sponsors/sponsor_form.html'
    model = Sponsor
    fields = ['type','name','image']
    success_url = reverse_lazy('sponsors:sponsors_list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class UpdateSponsor(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    template_name = 'sponsors/sponsor_form.html'
    model = Sponsor
    fields = ['name','image']
    success_url = reverse_lazy('sponsors:sponsors_list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class DeleteSponsor(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Sponsor
    success_url = reverse_lazy('sponsors:sponsors_list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff