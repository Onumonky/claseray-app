from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"type": "text", "class":"form-control"}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type": "password", "class":"form-control"}))
    


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control"}))
    paswword1 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control"}))
    paswword2 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control"}))
    first_name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control"}))
    last_name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={"type":"text", "class":"form-control"}))