from django.shortcuts import render, redirect
from django.db import connection
from django.urls import reverse,reverse_lazy
from django.contrib.auth import authenticate, login, logout 
from django.views.generic import CreateView, View
from django.contrib import messages
from django.contrib.auth.models import Group
from django.views.generic import (TemplateView, ListView)

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from .models import *
from events.models import EventRegistration
from competitions.models import CompetitionRegistration
from .forms import *

from events.models import EventRegistration
from competitions.models import CompetitionRegistration

from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

class SignUpView(UserPassesTestMixin, CreateView):
    form_class = CreateUserForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')
    def test_func(self):
        return self.request.user.is_anonymous
    

@login_required
def profile(request, pk=None):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('accounts:account_settings')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        all_events = EventRegistration.objects.filter(user=request.user)
        all_competition = CompetitionRegistration.objects.filter(user=request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'all_events': all_events,
        'all_competition':all_competition
    }
    return render(request, 'accounts/profile.html', context)


class ListUsers(ListView):
    model = User
    fields = ['username','email']
    template_name = 'accounts/users.html'
    context_object_name = 'customers'


def user_detail(request,pk):
    user = User.objects.get(id=pk)
    
    all_events = user.eventregistration_set.all()
    all_competitions = user.competitionregistration_set.all()

    context = {
        'all_events': all_events,
        'all_competitions': all_competitions
    }
    return render(request, 'accounts/user_detail.html', context)



# class UserDetail(ListView):
#     model = EventRegistration
#     fields = ['event']
#     template_name = 'accounts/events_registered.html'


# class LoginView(View):
#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return redirect('login')
#             else:
#                 messages.info(request, 'Username OR password is incorrect')

#         return render(request, "accounts/login.html")

# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         messages.info(request, "Logged out successfully!")
#         return redirect('login')

