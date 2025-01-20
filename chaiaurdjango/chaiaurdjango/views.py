from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello home")
    return render(request,"website/index.html")

def about(request):
    # return HttpResponse("about home")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("contact home")
    return render(request, 'website/contact.html')

def services(request):
    # return HttpResponse("services home")
    return render(request, 'website/services.html')
