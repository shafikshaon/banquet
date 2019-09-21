from django import forms
from django.contrib.auth import password_validation
from django.forms import ModelForm

from accounts.models import SystemUser


class SystemUserCreationForm(ModelForm):
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
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control emphasized',
                'placeholder': 'New password',
            }
        ),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control emphasized',
                'placeholder': 'Confirm new password',
            }
        ),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = SystemUser
        fields = ("first_name", "last_name", "username", "email")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
