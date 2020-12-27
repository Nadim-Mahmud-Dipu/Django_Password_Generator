from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random

def home(request):
    return render(request,'generator/home.html',{'password':'83jhfbvfj353!@#'})

def about(request):
    return render(request, 'generator/about.html')
def password(request):

    thePassword = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_+?[]|')

    length = int(request.GET.get('length',12))

    for x in range(length):
        thePassword += random.choice(characters)

    return render(request, 'generator/password.html',{'password': thePassword})