from django.urls import path
from .views import *


app_name = 'competitions'

urlpatterns = [
    path('', ListCompetition.as_view(), name="competitions_list"),
    path('add', AddCompetition.as_view(), name="add_competition"),
    path('<slug:slug>', UpdateCompetition.as_view(), name="update_competition"),
    path('delete/<slug:slug>', DeleteCompetition.as_view(), name="delete_competition"),    
]