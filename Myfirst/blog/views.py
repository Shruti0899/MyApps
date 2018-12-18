from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
import sqlite3 as sql

# Create your views here.
def home(request):
    return render(request,"blog/home.html")

def initial(request):
    return render(request,"blog/sign_up.html")

def sign_up(request):
    print("------------------",request.POST)
    uname = request.POST['name'];
    psw = request.POST['psw'];
    email = request.POST['emailid'];
    data=User.objects.create_user(username=uname,password=psw,email=email)
    data.save()
    return render(request,"blog/home.html")

def log(request):
    return render(request,"blog/login.html")

def log_in(request):
    user_name = request.POST['name'];
    psw = request.POST['psw'];
    data=User.objects.filter(username=user_name,password=psw)

    if data.exists():
        print("Inside if_____________________", data)
        return render(request,"blog/sign_up.html")
    else:
        print("Inside Else___________________", data)
        return render(request,"blog/login.html")






