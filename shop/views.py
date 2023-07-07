from django.shortcuts import render
from django.http import HttpResponse
from . models import Product,Contact,Orders,order_update
from math import ceil
import json

# Create your views here.
def index(request):
    products=Product.objects.all()
    n=len(products)
    nslides=n//4+ceil((n/4)-(n//4))
    allprod=[]
    catg_prod=Product.objects.values('category','id')
    categ={item['category']for item in catg_prod}
    for i in categ:
        prod=Product.objects.filter(category=i)
        allprod.append(prod)
    par={"no of slides":nslides,"range":range(1,nslides),"product":products,"prod":allprod}
    return render(request,'shop/index.html',par)
def home(request):
    return render(request,'shop/index.html')
def about(request):
    return render(request,'shop/about.html')
def order(request):
    return render(request,'shop/order.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'shop/contact.html')
def track(request):
    if request.method=="POST":
        ord_id=request.POST.get('ord_id','')
        email=request.POST.get('email','')
        try:
            order=Orders.objects.filter(ord_id=ord_id,email=email)
            print(order)
            while Orders.objects.filter(ord_id=ord_id,email=email).exists():
                updates=[]
                update= order_update.objects.filter(ord_id=ord_id)
                print(update)
                texts=[]
                times=[]
                text=order_update.objects.filter(ord_id=ord_id).values_list('update_desc')
                time=order_update.objects.filter(ord_id=ord_id).values_list('timestamp')
                for i in text:
                    texts.append(i)
                print(texts)
                for i in time:
                    times.append(i)
                print(times)
                for i in range(len(texts)):
                    print(texts[i],times[i])
                    updates.append({'text':texts[i],'time':times[i]})
                    print(updates)
                    response=json.dumps(updates,default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request,'shop/track.html')
def cart(request):
    if request.method=="POST":
        item_JSON=request.POST.get('item_JSON','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address','')+''+request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        pin_code=request.POST.get('pin_code','')
        phone=request.POST.get('phone','')
        order=Orders(item_JSON=item_JSON,name=name,email=email,address=address,city=city,state=state,pin_code=pin_code,phone=phone)
        order.save()
        update=order_update(ord_id=order.ord_id,update_desc="The Order has been placed")
        update.save()
        thank = True
        id = order.ord_id
        return render(request, 'shop/cart.html', {'thank': thank, 'id': id})
    return render(request,'shop/cart.html')
def productView(request,myid):
    product=Product.objects.filter(id=myid)
    return render(request,'shop/ProdView.html',{'product':product[0]})
