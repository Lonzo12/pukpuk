from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'd-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'd-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'd-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'd-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'd-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'd-input'}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

class CreateProduct(forms.ModelForm):
    name = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class': 'd-input'}))
    desc = forms.CharField(label='Описание', widget=forms.TextInput(attrs={'class': 'd-input'}))
    kol = forms.CharField(label='Количество', widget=forms.TextInput(attrs={'class': 'd-input'}))
    price = forms.CharField(label='Цена', widget=forms.TextInput(attrs={'class': 'd-input'}))
    class Meta:
        model = Products
        fields = ['pict', 'name', 'desc', 'kol', 'price']

class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Search')