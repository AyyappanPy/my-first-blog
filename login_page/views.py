from django.shortcuts import render, get_object_or_404
from .models import SignIn
from .forms import SignInForm

# Create your views here.

def login_page(request):
    if request.method == "POST":
        print request.POST, "<--------------------"
        # signin = get_object_or_404(SignIn)

        form = SignInForm(request.POST, instance=SignIn)
        if form.is_valid():
            form.save(commit=False)
        return render(request, 'login_page/sign_up.html', {})
    else:
        return render(request, 'login_page/sign_up.html', {})