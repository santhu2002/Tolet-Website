from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User ,auth

# Create your views here.

def login(request):
    if(request.method == 'POST'):
        username = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            # messages.info(request,"Invalid Credentials")
            return redirect('/login')
    return render(request,'Login.html')
def register(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        # phone = request.POST['phone']
        password = request.POST['password']
        if(User.objects.filter(username=name).exists() or User.objects.filter(email=email).exists() ):
            print("user already exist")
            # messages.info(request,"User Already Exist")
            return redirect('/')
        else:
            user = User.objects.create_user(username=name,password=password,email=email)
            user.save()
            print('user created')
            return redirect('/')
            # messages.info(request,"User Created")
        return redirect('/')
    return render(request,'Register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')