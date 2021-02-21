from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'accounts'

urlpatterns = [
    
    path('register/', SignUpView.as_view() , name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html", redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user', profile , name='account_settings'),
    path('dashboard', ListUsers.as_view() , name='user_page'),
    path('user_detail/<int:pk>', user_detail , name='user_details'),

]