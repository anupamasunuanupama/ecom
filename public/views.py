from django.shortcuts import render,redirect
from django.http import HttpResponse
from.forms import UserAddForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorators import admin_only,unauthenticated_user,allowed_user
from Product.models import ProductDetails


@admin_only
def Index(request):
    product = ProductDetails.objects.all()
    context = {
        "product":product
    }
    return render(request,"index.html",context)

@allowed_user
def AdminIndex(request):
    return render(request,"adminhome.html")

@unauthenticated_user
def SignIn(request):
    if request.method=="POST":
        username=request.POST["uname"]
        password=request.POST["pswd"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('Index')
        else:
            messages.info(request,"Username or password incorrect")
            return redirect('SignIn')
    return render(request,"login.html")

@unauthenticated_user
def SignUp(request):
    form=UserAddForm()
    if request.method=="POST":
        form =UserAddForm(request.POST)
        
        if form.is_valid():
            username=form.cleaned_data.get("username")
            email=form.cleaned_data.get("email")
            
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('SignUp')
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect("SignUp")
            else:
                form.save()
                messages.success(request,"User created")
                return redirect('SignIn')
            
    context={"form":form}
    return render(request,"register.html",context)

def SignOut(request):
    logout(request)
    return redirect('Index')
# Create your views here.
