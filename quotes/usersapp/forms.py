from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput())

    email = forms.CharField(max_length=100, required=True, widget=forms.TextInput())

    password1 = forms.CharField(
        max_length=50, required=True, label="Password", widget=forms.PasswordInput()
    )

    password2 = forms.CharField(
        max_length=50,
        required=True,
        label="Repeat password",
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
