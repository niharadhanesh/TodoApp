from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
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

from django.contrib.auth.decorators import login_required
from .models import Todo

@login_required
def dashboard(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Todo.objects.create(
                user=request.user,
                title=title
            )
        return redirect("dashboard")

    todos = Todo.objects.filter(user=request.user).order_by("-created_at")

    return render(request, "dashboard.html", {
        "todos": todos
    })


@login_required
def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)

    if request.method == "POST":
        todo.title = request.POST.get("title")
        todo.save()
        return redirect("dashboard")

    return redirect("dashboard")


@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect("dashboard")

from django.shortcuts import redirect
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('signin')   # redirect to signin page
