from django import forms
from .models import LogIn
from .models import SignUp
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class SignUpForm(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ('email', 'password', 'repeat_password')

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password' in self.cleaned_data and 'repeat_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['repeat_password']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

class LogInForm(forms.ModelForm):

    class Meta:
        model = LogIn
        fields = ('email', 'password')