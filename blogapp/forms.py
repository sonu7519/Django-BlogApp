from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

from django.utils.translation import gettext, gettext_lazy as _

from .models import Post

class signup(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First Name'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last Name'}),
        'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}),
        'Password': forms.TextInput(attrs={'class': 'form-control'}),
        'Confirm Password': forms.TextInput(attrs={'class': 'form-control'})
        }
    
class loginforms(AuthenticationForm):
    username = UsernameField(label="Username", widget=forms.TextInput(attrs={'autofocus': True, 'class': "form-control"}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class Postform(forms.ModelForm):
        class Meta:
            model = Post
            fields = ['title', 'desc']
            labels = {'title':'Title', 'desc': 'Description'}
            widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            }