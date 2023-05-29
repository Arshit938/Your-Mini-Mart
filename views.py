#   backup for views.py 
from email import message
from email.policy import default
from http.client import HTTPResponse
from math import ceil
from sqlite3 import paramstyle
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import product,cart,sign_in,query
from django.http import HttpResponseRedirect

def help(request):
    return render(request,'help.html')   

def nslides_cal(n) :
    if n == 3:
        slides = 1
    if(n%3 == 0) :
        slides = int(n/3)
    else :
        slides = int(n/3) + 1
    return slides    

def index(request) :
    products = product.objects.all()
   
    mens_fashion = []
    electro = []
    sports = []
    daily_use = []
    for i in products :
        if i.catagory == "men fashion" :
            mens_fashion.append(i)
        elif i.catagory == "electronics" :
            electro.append(i)
        elif i.catagory == "sports" :
            sports.append(i)
        elif i.catagory == "grocery" :
            daily_use.append(i)
        else :
            break                

    nprod = len(products)
    nMF = len(mens_fashion)
    nsports = len(sports)
    nelectro = len(electro)
    ndaily = len(daily_use)
    nslidesProd = nslides_cal(nprod)
    nslidesMF = nslides_cal(nMF)
    nslidesSports = nslides_cal(nsports)
    nslidesDaily = nslides_cal(ndaily)
    nslidesElectro = nslides_cal(nelectro) 
    cat_list=["Men's Fashion","Electronics","Gamming","smartphones","grocery","sports"]
    allprod = [
        [products,range(0,nslidesProd),nslidesProd],
        [mens_fashion,range(0,nslidesMF),nslidesMF],
        [electro,range(0,nslidesElectro),nslidesElectro],
        [sports,range(0,nslidesSports),nslidesSports],
        [daily_use,range(0,nslidesDaily),nslidesDaily]
    ]
    # params = {'prod' : prod,'no_of_slide' : nslides , 'range' : range(0,nslides),'iterator' : range(0,3)}
    params = {'allprod' : allprod,'cat':cat_list}
    return render(request,'shop/index.html',params)

# the function below is for both addtocart and view button
# def view_product(request) :
    # products = product.objects.all()
    
    # value = request.GET.get("view")
    # for i in products:
        # if value == i.product_name :
            # cat=i.catagory  
            # params = {'product' : i}        
    # return render(request,'shop/view_product.html',params)
# 
def view_product(request) :
    products = product.objects.all()
    # 
    value = request.GET.get("view")
    for i in products:
        if value == i.product_name :
            cat=i.catagory  
            p=i
    related_prod=[]        
    for i in products:
        if cat == i.catagory:
            related_prod.append(i)
    nslides=nslides_cal(len(related_prod)) 
    prod_info=[i,[related_prod,range(0,nslides),nslides]]       
    params={'product' : p,'related_prod' : related_prod,'range' : range(0,nslides),'nslides' : nslides}        
    return render(request,'shop/view_product.html',params)



def signup(request):
    return render(request,'signin.html')        

def search_product(request):
    lst=[]
    searchItem= request.GET.get("argument","default")
    products = product.objects.all()
    for i in products :
        if searchItem in i.product_name:
            lst.append(i)
        elif searchItem in i.sub_catagory :
            lst.append(i)
        elif searchItem in i.catagory :
            lst.append(i)
    params={'products' : lst}
    return render(request,'search_prod.html',params)                    

def addToCart(request):
    item=request.GET.get("add to cart")
    # id,image,catregory,name,price
    products=product.objects.all()
    for i in products:
        if i.product_name==item:
            obj=cart(image=i.product_image,category=i.catagory,name=i.product_name,price=i.price)
            obj.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'),message='added successfully')      

def Cart(request):
    items = cart.objects.all() 
    params={'items' : items}
    return render(request,'shop/cart.html',params)  

def Explore(request):
    products=product.objects.all()
    cat=request.GET.get("exp")
    pro=[]
    for i in products:
        if cat == i.catagory:
            pro.append(i)
    params={'products' : pro}
    return render(request,'shop/explore.html',params)   
   