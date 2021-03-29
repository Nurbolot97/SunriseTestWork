from django import forms
from django.forms import Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserAccount


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255, required=True,
                            widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('first_name', 'last_name', 'phone_number', 'biography', 'photo')
        widgets = {
            'biography': Textarea(attrs={'col': 80, 'rows': 2}),
        }