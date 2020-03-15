from django.shortcuts import render
import random

def home(request):
    return render(request, 'home/home.html')

def password(request):
    password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    l = int(request.GET.get('length',12))
    sc = bool(request.GET.get('special'))
    n = bool(request.GET.get('numbers',))
    u = bool(request.GET.get('uppercase',))

    if u:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if sc:
        characters.extend(list('!@#$%^&*()_+=?/><.,`~'))
    if n:
        characters.extend(list('1234567890'))

    for i in range(l):
        password += random.choice(characters)

    return render(request, 'home/password.html', {'password':password})


def about(request):
    return render(request, 'about/about.html')