from django.forms import ModelForm, EmailField
from django.contrib.auth.forms import AuthenticationForm
from flight.models import User
from django import forms

class UserSignUpForm(ModelForm):
    class Meta:
        model = User
        exclude = ['last_login']
    field_order = ['first_name', 'last_name', 'email' ,'password', 'phone_num']

class UserLoginForm(forms.Form):
    email = forms.EmailField(required=True)  
    password = forms.CharField(widget=forms.PasswordInput)
