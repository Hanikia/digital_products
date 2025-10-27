from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import RegisterForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('products:post_list')
    else:
        form = RegisterForm()
    
    return render(request, "users/register.html", {"form": form})


def Login_View(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
           user = form.get_user()
           login(request , user)
           return redirect("/posts")
    else: 
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form":form})


def Logout_View(request):
    if request.method == "POST":
        logout(request)
        return redirect("/posts")
    return render(request, "users/logout.html")