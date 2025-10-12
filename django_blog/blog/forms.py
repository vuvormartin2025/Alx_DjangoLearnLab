from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Registration form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Profile update form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']