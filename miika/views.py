
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, RequestContext

# View for the home Page

def home(request):
    # return render(request, 'home.html')
    return render(request, 'miika/home.html')

def about(request):
    return render(request, 'miika/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'miika/contact.html', {'title': 'Contact'})
