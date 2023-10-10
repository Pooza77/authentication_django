from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import path 
from app1 import views 
from django.contrib.auth.models import User
from django.shortcuts import redirect,render
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def home(request):
     return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse("Password donot match!!!!!!!")
        else:
            user = User.objects.create_user(username, email, pass1)
            user.save()
            return redirect('login')
    return render(request, 'signup.html')

def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
           return HttpResponse("Username and password donot match each other!!!")
         
    return render(request,'login.html')
