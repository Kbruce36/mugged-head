from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def pricing(request):
    return render(request, 'pricing.html')

def about(request):
    return  render(request, 'about.html')