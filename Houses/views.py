from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User ,auth
from Home.models import Enterhome

# Create your views here.
def enterhome(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        desc = request.POST['desc']
        location = request.POST['location']
        price = request.POST['price']
        offer =True
        img = request.POST['img']
        en=Enterhome(name=name,desc=desc,location=location,price=price,offer=offer,img=img)
        en.save()
    return render(request,'Enterhome.html')
def ourhomes(request):
    homes=Enterhome.objects.all()
    return render(request,'Ourhomes.html',{'homes':homes})