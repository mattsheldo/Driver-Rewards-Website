from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
#from . import AccountChecks
from .forms import UserRegisterForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        return render(request, 'homepage/homepage.html')
        #if form.is_valid():
            #username=form.cleaned_data.get('username')
            #password=form.cleaned_data.get('password')
            #accCheck = AccountChecks.verifyAccount(username, password)
            #if accCheck == true:
                #return render(request, 'homepage/homepage.html')
            #else:
             #   return render(request, 'login/login.html')
    else:
        form = AuthenticationForm()
        return render(request, 'login/login.html', {'form':form})
        

def createAcc(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #if form.is_valid():
           # form.save()
            #username = form.cleaned_data.get('username')
            #password = form.cleaned_data.get('password')
        return render(request, 'homepage/homepage.html' )
    else: 
        form = UserRegisterForm()
        return render(request, 'createAcc/register.html', {'form':form})

def logout(request):
    return render(request, 'logout/logout.html')

def home(request):
    return render(request, 'homepage/homepage.html')
