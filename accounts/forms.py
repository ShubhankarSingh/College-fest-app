from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms

from .models import Profile



class CreateUserForm(UserCreationForm):
	class Meta:
		model = get_user_model()
		fields = ['username', 'email', 'password1', 'password2']
        
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email']
        help_texts = {
            'username': None,
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']