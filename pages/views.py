
from django.shortcuts import render
from django.views import View
# Create your views here.
def homepage_render(request):
    return render(request,'homepage.html')

class esewa(View):
    def get(self, request, *args, **kwargs):
            context = {
                
            }
            return render(request, 'payments.html', context)
