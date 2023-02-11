from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User ,auth
from Home.models import Enterhome
from geopy.geocoders import ArcGIS

# Create your views here.
def enterhome(request):
    if request.user.is_authenticated:
        if(request.method == 'POST'):
            name = request.POST['name']
            desc = request.POST['desc']
            location = request.POST['location']
            loc=ArcGIS()
            # loc = Nominatim(user_agent="GetLoc")
            getLoc = loc.geocode(location)
            # longitude = request.POST['longitude']
            # latitude = request.POST['latitude']
            print(getLoc)
            if(request.POST['longitude']):
                longitude = request.POST['longitude']
                latitude = request.POST['latitude']
            else:
                longitude = getLoc.longitude
                latitude = getLoc.latitude
            price = request.POST['price']
            offer =request.POST.get('offer',False)
            img = request.FILES['img']
            en=Enterhome(name=name,desc=desc,location=location,price=price,offer=offer,img=img,longitude=longitude,latitude=latitude)
            en.save()
            return render(request,'Enterhome.html')
        else:
            return render(request,'Enterhome.html')
    else:
        messages.info(request,"Please Login/Register To Add a Home")
        return redirect('/accounts/login')
def ourhomes(request):
    if request.user.is_authenticated:
        homes=Enterhome.objects.all()
        return render(request,'Ourhomes.html',{'homes':homes})
    else:
        messages.info(request,"Please Login/Register To See Our Homes")
        return redirect('/accounts/login')
