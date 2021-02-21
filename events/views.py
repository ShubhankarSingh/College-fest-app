from django.shortcuts import render, redirect 
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect, HttpRequest
from django.views.generic import (TemplateView, ListView,
                                  CreateView, UpdateView,
                                  DetailView, DeleteView, FormView)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import *


class ListEvent(LoginRequiredMixin ,ListView):
    template_name = 'events/event_dashboard.html'
    model = Event
    context_object_name = 'events'


class AddEvent(LoginRequiredMixin, UserPassesTestMixin ,CreateView):
    template_name = 'events/event_form.html'
    model = Event
    fields = ['id','title','description','image','time','is_online','meet_link']
    success_url = reverse_lazy('events:events_list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class UpdateEvent(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    template_name = 'events/event_form.html'
    model = Event
    fields = ['title','description','image','time','is_online','meet_link']
    success_url = reverse_lazy('events:events_list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class DeleteEvent(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Event
    success_url = reverse_lazy('events:events_list')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


def event_add_attendance(request, pk):
    this_event = Event.objects.get(pk=pk)
    this_event.add_user_to_list_of_attendees(user=request.user)
    return redirect('events:events_list')