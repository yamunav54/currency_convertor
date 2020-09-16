from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    terms_confirmed = forms.BooleanField(help_text='I confirm all the term and conditions')

    class Meta:
        model = User
        fields = ('username',  'password1', 'password2', 'terms_confirmed')