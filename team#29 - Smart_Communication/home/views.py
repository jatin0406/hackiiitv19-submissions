# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import *


# Create your views here.
 
def add(request):
    # return render(request,"bhai kuch nahi hai")
    # if (request.method=='POST'):
    #     num1=request.POST['num1']     
    #     num2=request.POST['num2'] 
    #     num1=int(num1)
    #     num2=int(num2)
    #     return HttpResponse(num1+num2)

    
    # return render(request,"sum/add.html") 
    return render(request,"home/guide.html") 
def guideA(request):
    
    
    if(request.method=='POST'):
        

        form1=Productform(request.POST)
        if form1.is_valid():
            form1.save()
          
    else:
      form1=Productform()
      
      
    data=Product2.objects.all()
        
        
           
    return render(request,"home/guideA.html",{'form':form1,'msg':data})  
def guideB(request):
    
    if(request.method=='POST'):
        

        form=Productform2(request.POST)
        if form.is_valid():
            form.save()
          
    else:
        form=Productform2()
    data=Product.objects.all()
    

    
    return render(request,"home/guideB.html",{'form':form,'msg':data})  