from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')
def register(request):
    return render(request, 'register.html')
def success(request):
    return render(request, 'success.html')