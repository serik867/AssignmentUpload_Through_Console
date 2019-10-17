from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def home(request):
    return render(request,'index.html')


def login(request):
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    if username=="Serdar" and password=="12345" and email=="serdar12345@gmail.com":
        return render(request,'login.html',{'username':username,'email':email})
    else:
        return HttpResponse("Sorry wrong")