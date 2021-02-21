from django.urls import path
from .views import *


app_name = 'sponsors'

urlpatterns = [
    path('', ListSponsor.as_view(), name="sponsors_list"),
    path('add', AddSponsor.as_view(), name="add_sponsor"),
    path('<slug:slug>', UpdateSponsor.as_view(), name="update_sponsor"),
    path('delete/<slug:slug>', DeleteSponsor.as_view(), name="delete_sponsor"),
]