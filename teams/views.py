from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect, HttpRequest
from .models import *
from django.views.generic import (TemplateView, ListView,
                                  CreateView, UpdateView,
                                  DetailView, DeleteView)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin                            

class ListTeam(LoginRequiredMixin, ListView):
    template_name = 'teams/team_dashboard.html'
    model = Team
    context_object_name = 'teams'

    def get_context_data(self, **kwargs):
        context = super(ListTeam, self).get_context_data(**kwargs)
        context['team_types'] = TeamType.objects.all()

        return context


class AddTeam(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'teams/team_form.html'
    model = Team
    fields = ['type','name','image']
    success_url = reverse_lazy('teams:teams_list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class UpdateTeam(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    template_name = 'teams/team_form.html'
    model = Team
    fields = ['name','image']
    success_url = reverse_lazy('teams:teams_list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class DeleteTeam(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Team
    success_url = reverse_lazy('teams:teams_list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff