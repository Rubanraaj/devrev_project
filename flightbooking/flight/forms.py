from django.forms import ModelForm, EmailField
from django.contrib.auth.forms import AuthenticationForm
from flight.models import User
from django import forms

class UserSignUpForm(ModelForm):
    class Meta:
        model = User
        exclude = ['last_login', 'is_active', 'is_superuser','is_staff']
    field_order = ['first_name', 'last_name', 'email' ,'password', 'phone_num']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('groups')
        self.fields.pop('user_permissions')

class UserLoginForm(forms.Form):
    email = forms.EmailField(label="Email")  
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'autofocus': True})

class FlightSearchForm(forms.Form):
    date = forms.DateField()
    time = forms.TimeField()
