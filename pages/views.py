
from django.shortcuts import render
from django.views import View
# Create your views here.


def homepage_render(request):
    return render(request,'homepage.html')

