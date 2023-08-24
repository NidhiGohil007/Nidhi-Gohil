from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
# Create your views here.

def data(request):
    return HttpResponse('<h1>this is my first webpage<h1>')

def login(request):
    return render(request,'login.html')

def index(request):
    a=Category.objects.all()
    return render(request,'index.html',{'data':a})

def allproduct(request):
    a=Product.objects.all()
    return render(request,'product.html',{'data':a})


def filterproduct(request,id):
    a=Product.objects.filter(categoryname=id)
    return render(request,'product.html',{'data':a})