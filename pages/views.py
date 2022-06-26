
from django.shortcuts import render
from django.views import View
# Create your views here.

context_menus = {
    "Food for the animal shelter":{"name":"Animal Food","description":"Feed the hungry dogs at the animal shelter","image":"/images/animal.png"},
    "Donate to charity":{"name":"Be the Medic","description":"Donate to the cancer patients and its research","image":"/images/money.png"},
    "Provide to feed a family":{"name":"Feem them wont ya?","description":"Quench the hunger of the poor"},
    "Plant a tree":{"name":"Reduce their print","description":"Plant a tree in someones name to forever be a part of the world","image":"/images/plant.png"},
    "Build a well in africa":{"name":"Water for Everyone","description":"Chip in to help build a well in very rural parts of the world","image":"/images/well.png"},
    "Help a student with his needs":{"name":"Educate One Educate All","description":"Provide to pay for someones college even the tinniest bit helps","image":"/images/scholarship.png"},
    }

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


def payment_render(request):
    if request.method=="POST":
        animal = request.POST.get("food_animal")
        donate = request.POST.get("charity_money")
        tree = request.POST.get("tree_plant")
        water = request.POST.get("water_well")
        scholarship = request.POST.get("scholarship")
        food = request.POST.get("food_bank")
        result = 0
        for i in [animal,donate,tree,water,scholarship,food]:
            if i!= None:
                result = i
        result = context_menus[result]
        context=result
        return render(request,"payment.html",context)
    context={}
    return render(request,"payment.html",context)