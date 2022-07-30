import re
from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpResponse
import pymongo

# Create your views here.
cli=pymongo.MongoClient("mongodb://localhost:27017")
mydba=cli['login']
mytba=mydba['CRED']

def home(request):
    return HttpResponse("<h1>Hello World</h1>")

def login(request):
     return render(request,"index.html")

def req(request):
    USER=request.COOKIES['Username']

    data={
        'user':USER
    }
    response=render(request,"home.html",data)
    return response


def CRED(request):
    user=request.POST.get('user')
    passw=request.POST.get('pass')
    if user=="Admin" and passw=="pass":
         response=redirect('home/')
         response.set_cookie("Username",user)
         response.set_cookie('Password',passw)
         return response
    else:
        return redirect('/')


    

def logout(request):
    response=redirect('cred/home/')
    response.delete_cookie('Username')
    response.delete_cookie('Password')
   

    return redirect("/")