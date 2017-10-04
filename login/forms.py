from django import forms
from django.contrib.auth import (
		authenticate,
		get_user_model,
		login,
		logout,
	)

User = get_user_model()


class Login(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','password','first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }
