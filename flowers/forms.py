from django.contrib.auth.forms import UserCreationForm
from django import forms


class ARegistrationForm(UserCreationForm):
    email = forms.CharField(label="Email", max_length=100)