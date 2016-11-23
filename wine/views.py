from django.shortcuts import render

# Create your views here.

def wine_page(request):
    return render(request, 'wine/index.html', {})