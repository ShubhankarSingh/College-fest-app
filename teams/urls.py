from django.urls import path
from .views import *


app_name = 'teams'

urlpatterns = [
   path('', ListTeam.as_view(), name="teams_list"),
    path('add', AddTeam.as_view(), name="add_team"),
    path('<slug:slug>', UpdateTeam.as_view(), name="update_team"),
    path('delete/<slug:slug>', DeleteTeam.as_view(), name="delete_team"),
]