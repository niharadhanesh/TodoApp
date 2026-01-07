from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.


def signin(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user:
            auth_login(request, user)
            return redirect("dashboard")

    return render(request, "signin.html")


def signup(request):
   if request.method == "POST":
       
       username = request.POST.get("username")
       password = request.POST.get("password")
       cpassword = request.POST.get("cpassword")

       if password != cpassword :
           return render(request, "signup.html" , {"error":"password do not match"})
       
       user = User.objects.create_user(
           username = username,
           password =password
       )

       Profile.objects.create(user=user,)
       return redirect("signin")
   
   return render(request,"signup.html")

def dashboard(request):
    return render(request, "dashboard.html")