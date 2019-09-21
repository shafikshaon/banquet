from django import forms
from django.contrib.auth import password_validation
from django.forms import ModelForm

from accounts.models import SystemUser


class SystemUserChangeForm(ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control emphasized',
                'autofocus': 'autofocus',
                'placeholder': 'First name',
                'autocomplete': 'off'
            }
        ),
        error_messages={'required': 'Please enter first name'},
        required=True
    )
    last_name = forms.CharField(
        label='Last name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control emphasized',
                'placeholder': 'Last name',
                'autocomplete': 'off'
            }
        ),
        error_messages={'required': 'Please enter last name'},
        required=True
    )
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control emphasized',
                'placeholder': 'Username',
                'autocomplete': 'off'
            }
        ),
        error_messages={'required': 'Please enter username'},
        required=True
    )
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control emphasized',
                'placeholder': 'Email',
                'autocomplete': 'off'
            }
        ),
        error_messages={'required': 'Please enter email', 'unique': 'Email already exists.'},
        required=True
    )

    class Meta:
        model = SystemUser
        fields = ("first_name", "last_name", "username", "email")
