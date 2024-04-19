import hashlib
from random import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from users.models import User, UserProfile


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput
        (attrs={'class': 'form-control py-4', "placeholder": "Введите имя пользователя"}))
    password = forms.CharField(widget=forms.PasswordInput
        (attrs={'class': 'form-control py-4', "placeholder": "Введите  пароль"}))

    class Meta:
        model = User
        fields = ("username", "password")


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput
        (attrs={'class': 'form-control py-4', "placeholder": "Введите имя пользователя"}))
    first_name = forms.CharField(widget=forms.TextInput
        (attrs={'class': 'form-control py-4', "placeholder": "Введите имя"}))
    last_name = forms.CharField(widget=forms.TextInput
        (attrs={"class": 'form-control py-4', "placeholder": "Введите фамилию"}))
    email = forms.CharField(widget=forms.EmailInput
        (attrs={'class': 'form-control py-4', "placegolder": "Введите адрес эл. почты"}))
    password1 = forms.CharField(widget=forms.PasswordInput
        (attrs={'class': 'form-control py-4', "placeholder": "Введите  пароль"}))
    password2 = forms.CharField(widget=forms.PasswordInput
        (attrs={'class': 'form-control py-4', "placeholder": "Введите  пароль"}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save()
        user.is_active = False
        salt = hashlib.sha1(str(random()).encode('utf-8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf-8')).hexdigest()
        user.save(update_fields=['is_active', 'activation_key'])
        return user


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput
    (attrs={'class': 'form-control py-4', "placeholder": "Введите имя пользователя", "readonly": True}), )
    first_name = forms.CharField(widget=forms.TextInput
    (attrs={'class': 'form-control py-4', "placeholder": "Введите имя"}))
    last_name = forms.CharField(widget=forms.TextInput
    (attrs={"class": 'form-control py-4', "placeholder": "Введите фамилию"}))
    email = forms.CharField(widget=forms.EmailInput
    (attrs={'class': 'form-control py-4', "placegolder": "Введите адрес эл. почты", "readonly": True}))
    image = forms.ImageField(widget=forms.FileInput
    (attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "image")

class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('about', 'gender')