from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
from django.contrib.auth import authenticate
# Create your views here.
def loginuser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password =request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request,"login.html")

    return render(request,"login.html")
def index(request):
    if request.user.is_authenticated:
        return  render(request,"index.html")
    else:
        return redirect("/login")
    return render(request,"index.html")
def logoutuser(request):
    logout(request)
    return redirect(request,"login.html")