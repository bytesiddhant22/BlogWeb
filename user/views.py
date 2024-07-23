from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        usersave = User.objects.create_user(username=username , email=email , password=password)
        usersave.save()

        messages.success(request , "Account created successfully , Now Log in ")
        return redirect('/')
    else:
        return render(request , 'signup.html')
    
def loginReq(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        loginUsername = request.POST['username']
        loginPassword = request.POST['password']

        loginUser = authenticate(request , username = loginUsername , password = loginPassword)
        if loginUser is not None:
            userl = login(request , loginUser)
            messages.success(request , "You are successfully logged in !")
            return redirect('/')
        else:
            messages.info(request , "Username or Password is incorrect !")
            return redirect('loginReq')


    return render(request , 'login.html')

def logoutReq(request):
    logout(request)
    messages.success(request, "Logged out successfully !")
    return redirect('/')