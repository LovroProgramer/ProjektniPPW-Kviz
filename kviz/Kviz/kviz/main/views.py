from django.shortcuts import render, redirect
from django.views.generic import ListView
from main.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

class KvizList(ListView):
    model = Kviz

class OsobaList(ListView):
    model = Osoba

class OdgovoriList(ListView):
    model = Odgovori

class PitanjaList(ListView):
    model = Pitanja