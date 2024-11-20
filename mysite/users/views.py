from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account created successfully')
            return redirect('food:index')
        else:
            return render(request,'user/register.html',{'form':form})
        
    else:
        form = RegisterForm()
        return render(request,'user/register.html',{'form':form})
