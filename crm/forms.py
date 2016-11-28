from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class LoginForm(forms.Form):
    #--------comments------------#
    # Creates Login Form
    #login is a custom form
    #----------------------------#
    
    username = forms.CharField(label = "Username", max_length = 80, required=True,
                       error_messages = {'required': 'Please enter username',
                                         'max_length': 'Username should not exceeds 80 chars'},
                      widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
               )
    password = forms.CharField(label = "Password", max_length = 100,
                       error_messages = {'required': 'Please enter password',
                                         'max_length': 'Password should not exceeds 100 chars'},
                       widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
               )

