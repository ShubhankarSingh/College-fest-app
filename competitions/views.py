from django.shortcuts import render, redirect 
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (TemplateView, ListView,
                                  CreateView, UpdateView,
                                  DetailView, DeleteView, FormView)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import *
import razorpay


class ListCompetition(LoginRequiredMixin ,ListView):
    template_name = 'competitions/competition_dashboard.html'
    model = Competition
    context_object_name = 'competitions'


class AddCompetition(LoginRequiredMixin, UserPassesTestMixin ,CreateView):
    template_name = 'competitions/competition_form.html'
    model = Competition
    fields = ['title','description','image','time','venue','seats']
    success_url = reverse_lazy('competitions:competitions_list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class UpdateCompetition(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    template_name = 'competitions/competition_form.html'
    model = Competition
    fields = ['title','description','image','time','venue','seats']
    success_url = reverse_lazy('competitions:competitions_list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class DeleteCompetition(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Competition
    success_url = reverse_lazy('competitions:competitions_list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff



