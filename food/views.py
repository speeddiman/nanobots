from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request , "food/index.html" )

def contactus(request):
    return render(request , "food/contactus.html")