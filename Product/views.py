from django.shortcuts import render,redirect, HttpResponse
from .forms import ProductAddForm
from django.contrib import messages
from .models import ProductDetails
from django.contrib.auth.decorators import login_required

def AddProduct(request):
    form = ProductAddForm()
    if request.method == "POST":
        form = ProductAddForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save()
            product.Merchant = request.user
            product.save()
            
            messages.info(request,"Product Added")
            return redirect("AddProduct")
        else:
            HttpResponse("INVALID")
    context ={
        "form":form
    }
    return render(request,"addproduct.html",context)

def ProductViewMerchant(request):
    products=ProductDetails.objects.all()
    context ={
        "products":products
    }
    return render(request,'productlist.html',context)

def DeleteProduct(request,pk):
    product=ProductDetails.objects.get(Product_Id = pk)
    product.Product_Image.delete()
    product.delete()
    messages.info(request,"Product deleted")
    return redirect("ProductViewMerchant")
    
def UpdateProduct(request,pk):
    product =ProductDetails.objects.filter(Product_Id = pk)
    if request.method == "POST":
        
        pname=request.POST['pname']
        pbrand=request.POST["pbrand"]
        pdis=request.POST["pdis"]
        pcat=request.POST["pcat"]
        price=request.POST["price"]
        pstock=request.POST["pstock"]
        image=request.FILES["image"]
        
        item=ProductDetails.objects.get(Product_Id = pk)
        
        item.Product_Name=pname
        item.Product_Brand=pbrand
        item.Product_Discription=pdis
        item.Product_Category=pcat
        item.Product_Price=price
        item.Product_stock=pstock
        item.Product_Image=image
        item.save()
        messages.info(request,"Item Updated")
        return redirect("UpdateProduct",pk=pk)
    context ={
        "product":product
    }
    return render(request,'updateproduct.html',context)

@login_required(login_url="SignIn")
def ViewProduct(request,pk):
    product=ProductDetails.objects.filter(Product_Id= pk)
    context={
        "product":product
    }
    return render(request,"viewproduct.html",context)

# Create your views here.
