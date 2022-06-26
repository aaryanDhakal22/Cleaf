
from django.shortcuts import render
from django.views import View
# Create your views here.


def homepage_render(request):
    # This implementation can be made further better with proper authentication
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "aaryan" and password =="hack2022":
            context={"name":"Aaryan"}
            return render(request,'homepage.html',context)
        else:
            context={"error":"Invalid Password"}
            return render(request,"error.html",context)
    return render(request,"login.html")

def donate_render(request):
    return render(request,"donate.html")

def login_render(request):
    return render(request,"login.html")


def payment_render(request,):
    if request.method=="POST":
        name = request.POST["name"]
    context={}
    return render(request,"payment.html",context)