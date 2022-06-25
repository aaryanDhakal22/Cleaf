from django.shortcuts import render

# Create your views here.
def homepage_render(request):
    return render(request,'homepage.html')

    