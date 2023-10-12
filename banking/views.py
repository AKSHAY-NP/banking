from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect
from .models import PersonalInfo
from django.contrib.auth.decorators import login_required
from urllib.parse import urlencode

# Create your views here.
def homepage(request):
    return render(request,'index.html',{})

@login_required(login_url='/login/')
def dashboard(request):
    context={}
    return render(request,'single.html',context)

@login_required(login_url='/login/')
def personal_info(request):
    if request.method=='POST':
        info=PersonalInfo.objects.create(
            name=request.POST['name'],
            dob=request.POST['dob'],
            age=request.POST['age'],
            gender=request.POST['gender'],
            phone_number=request.POST['phone'],
            email=request.POST['email'],
            address=request.POST['address'],
            district=request.POST['district'],
            branch=request.POST['branch'],
            account_type=request.POST['accountType'],
            materials_provide=request.POST['materials'] if 'materials' in request.POST else ""
         )
        info.save
        messages.success(request, "Personal information submitted successfully.")
        params = urlencode({'success_message': 'Personal information submitted successfully.'})
        return redirect('/message?' + params)
    return render(request,"personal_info.html",{})

@login_required(login_url='/login/')
def message(request):
    success_message = request.GET.get('success_message', None)
    context = {
        'success_message': success_message,
    }
    return render(request,'message.html',context)

def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password_confirm=request.POST['password_confirm']
        if password==password_confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username already exist')
                return redirect('/registration/')
            else:
                user=User.objects.create_user(password=password,username=username)
                user.save
                print("User Registered")
        else:
            print("Wrong Password")
            messages.error(request,"Wrong Password")
            return redirect('/registration/')
        return redirect('/login/')
    return render(request,"registration.html",{})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/dashboard/')
        else:
            messages.error(request,'Invalid Credential')
            return redirect('/login/')
    return render(request,"login.html",{})

def logout(request):
    auth.logout(request)
    return redirect("/")