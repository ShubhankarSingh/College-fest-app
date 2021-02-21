from django.urls import path
from .views import *


app_name = 'events'

urlpatterns = [
    path('', ListEvent.as_view(), name="events_list"),
    path('add', AddEvent.as_view(), name="add_event"),
    path('<slug:slug>', UpdateEvent.as_view(), name="update_event"),
    path('delete/<slug:slug>', DeleteEvent.as_view(), name="delete_event"),
    path('register_for_event/<int:pk>',event_add_attendance, name="register_event"),       
]