from django.shortcuts import render, get_object_or_404
# from .models import SignUp
from .forms import SignUpForm
from .forms import LogInForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponsePermanentRedirect

# Create your views here.

def login_page(request):
    if request.method == "POST":
        # signin = get_object_or_404(SignIn)
        if request.POST.get('commit') == 'Create Account':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                username=form.cleaned_data['email'].split('@')[0],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
                )
                return HttpResponsePermanentRedirect(reverse('wine:wine_page'))
            return render(request, 'login_page/sign_up.html', {})
        else:
            if request.POST.get('commit') == 'Log In':
                form = LogInForm(request.POST)
                if form.is_valid():
                    username = form.cleaned_data['email'].split('@')[0]
                    password = form.cleaned_data['password']
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return HttpResponsePermanentRedirect(reverse('wine:wine_page'))
            return render(request, 'login_page/sign_up.html', {})

    else:
        return render(request, 'login_page/sign_up.html', {})

