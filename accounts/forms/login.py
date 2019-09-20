from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _

__author__ = 'Shafikur Rahman'


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label='Username/ Email',
        widget=forms.TextInput(
            attrs={'class': 'form-control emphasized', 'autofocus': True, 'placeholder': 'Username/ Email'}
        )
    )

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control emphasized', 'placeholder': 'Password'}),
    )
