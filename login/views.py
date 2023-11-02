from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def create_user(request):
    print("asdff")
    if request.method == 'POST':
        print("tyr")
        form = UserCreationForm(request.POST)
        print("tyuy")
        if form.is_valid():
            print("yes")
            form.save()
            return redirect('login')
        else:
            return HttpResponse("not valid")
    else:
        form = UserCreationForm()
        return render(request,'create_user.html', {'form': form})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid details")
            return redirect('login')
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

