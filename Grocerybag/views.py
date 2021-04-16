from django.shortcuts import render,redirect
from Grocerybag.models import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'home.html')
def user_login(request):
    return render(request,'user_login.html')
def user_signup(request):
    return render(request,'user_signup.html')
def user_signup(request):
    error=""
    if request.method=='POST':
       f= request.POST['fname']
       l= request.POST['lname']
       p= request.POST['pwd']
       e= request.POST['email']
       con= request.POST['contact']
       gen= request.POST['gender']
       try:
           user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p,email=e)
           NUser.objects.create(user=user,mobile=con,gender=gen)
           error="no"
       except:
           error="yes"
    d ={'error':error}
    return render(request,'user_signup.html',d)
def user_login(request):
    error=""
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            login(request, user)
            error = "no"
        except:
            error = "yes"
    d={'error':error}
    return render(request,'user_login.html',d)
def Logout(request):
    logout(request)
    return redirect('home')
def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request,'user_home.html')
def add(request):
    if request.method=='post':
        it=request.POST['itemname']
        itq= request.POST['itemquantity']
        st=request.POST['status']
        d=request.POST['date']
        Add.objects.create(itemname=it,itemquantity=itq,date=d,status=st)

    return render(request,'add.html')
def index(request):
    data=Add.objects.all()
    d={'data':data}
    return render(request,'index.html',d)
def update(request):
    return render(request,'update.html')
