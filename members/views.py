from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')
    


def logout_(request):
    logout(request)
    messages.error(request, 'Logged out')
    return redirect('login')



def register_(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            username = request.POST['username']
            password = request.POST['password1']
            password1 = request.POST['password2']
            # firstname = request.POST['firstname']
            # lastname = request.POST['lastname']
            # email = request.POST['email']

            user = authenticate(username=username, password=password, password1=password1)
            login(request, user)
            messages.success(request, 'Successfully registred')
            return redirect('home')
    else:
        form = UserCreationForm()
        
    context = {'form': form}
    return render(request, 'register.html', context)