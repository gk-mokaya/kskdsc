from django.shortcuts import render

from django.views import View

# Create your views here.


def servicesView(request):   
    return render(request,'servicestemp/service.html')