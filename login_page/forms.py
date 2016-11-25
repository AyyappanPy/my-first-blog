from django import forms
from .models import SignIn

class SignInForm(forms.ModelForm):

    class Meta:
        model = SignIn
        fields = ('email', 'password', 'repeat_password')