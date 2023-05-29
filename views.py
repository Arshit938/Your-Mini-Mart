from django.http import HttpResponse
from django.shortcuts import render,redirect
from shop.models import product,cart
from shop import views

def index(request) :
    return render(request,'index.html')

def contact(request) :
    return render(request,'contact.html')

def about(request) :
    return render(request,'about.html')
def help(request):
    return render(request,'help.html')   

def signin(request) :
    return render(request,'signin.html')            

def search(request) :
    # lst=[]
    # searchItem= request.GET.get("argument","default")
    # products = product.objects.all()
    # for i in products :
    #     if searchItem in i.product_name:
    #         lst.append(i)
    #     elif searchItem in i.sub_catagory :
    #         lst.append(i)
    #     elif searchItem in i.catagory :
    #         lst.append(i)
    # params={'products' : lst}
    # return render(request,'search_prod.html',params) 
    return views.search_product(request)                   
def vp(request):
    # products = product.objects.all()
    # value = request.GET.get("view")    
    # for i in products:
    #     if value == i.product_name :
    #         params = {'product' : i}
            # return render(request,'shop/view_product.html',params)
    return views.view_product(request)        
def addToCart(request):
    products=product.objects.all()
    value=request.GET.get("add to cart")
    for i in products:
        if i.product_name==value:
            obj=cart(image=i.product_image,category=i.catagory,name=i.product_name,price=i.price)
            obj.save()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'),message='added successfully')      
            
def signup(request):
    return render(request,'signin.html')     

def Cart(request):
    items = cart.objects.all() 
    params={'items' : items}
    return render(request,'cart.html',params)

def del_prod(request):
    items=cart.objects.all()
    value=request.GET.get('del')
    for i in items:
        if i.name==value:
            i.delete()
            break
    return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))    
