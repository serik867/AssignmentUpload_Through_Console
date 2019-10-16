from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'Serdar'})


def login(request):
    username=request.POST['username']
    password=request.POST['password']
    email=request.POST['email']

    if username=="Serdar" and password=="12345" and email=="serdar12345@gmail.com":
        return render(request,'login.html',{'username':username,'email':email})
    else:
        return HttpResponse("Sorry wrong")