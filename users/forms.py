from django.contrib.auth.forms import UserCreationForm
from django import forms


class ARegistrationForm(UserCreationForm):
    email = forms.CharField(label="Email", max_length=100)
    first_name = forms.CharField(label="First name", max_length=100)