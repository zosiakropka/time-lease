"""@package account.forms
@author: Zosia Sobocinska
@date Dec 8, 2013
"""
from django import forms
from django.contrib.auth.models import User
from account.models import UserProfile


class UserSignUpForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    def clean_username(self):
        data = self.cleaned_data
        try:
            User.objects.get(username=data['username'])
        except User.DoesNotExist:
            return data['username']
        raise forms.ValidationError('This username is already taken.')

    def clean(self):
        try:
            data = self.cleaned_data
            if 'password' not in data or 'password_confirm' not in data:
                raise forms.ValidationError("Empty password")
            if data['password'] != data['password_confirm']:
                raise forms.ValidationError("Passwords entered do not match")
        except KeyError:
            pass
        return self.cleaned_data

    def save(self):
        data = self.cleaned_data
        user = User.objects.create(username=data['username'], password=data['password'])

        UserProfile.objects.create(user, email=data['email'])
