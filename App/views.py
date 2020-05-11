from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("点击")


def hehe(request):
    return HttpResponse("aini")

def gg(request):
    return render(request, "gg.html")

def hh(request):
    return render(request,"hh.html")