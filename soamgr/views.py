from django.shortcuts import render, redirect


def index(request):
    return redirect('soamgr:home')


def home(request):
    return render(request, 'soamgr/110-home.html')
