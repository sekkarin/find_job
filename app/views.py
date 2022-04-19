from django.shortcuts import render , HttpResponse ,redirect
# from app.models import User
from django.contrib.auth.models import User ,auth
from django.contrib.auth import authenticate
from company.models import *
from .forms import UploadFile


# Create your views here.
def index(request):
    jobs = Job.objects.all()
    
    return render(request, 'pages/index.html',{"jobs":jobs.values(),"totle_job":jobs.count()})

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        user = authenticate(username=username, password= pwd)
        if  user is not None:
            auth.login(request, user)
            print("เข้าสู่ระบบ สำเร็จ")
            return redirect('index')
        else:
            return render(request, 'pages/login.html',{"err":"มีข้อผิดพลาด"})
        
    return render(request,'pages/login.html')

def register(request):

    if request.method == "POST":
        email = request.POST.get('email')
        email_conf = request.POST.get('confirm_email')
        pwd = request.POST.get('pwd')
        pwd_conf = request.POST.get('confirm_pwd')
        username = request.POST.get('username')
        check_service = request.POST.get('check_service')
        
        if (email == email_conf and pwd == pwd_conf and username != "") :
            if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
                return render(request, 'pages/register.html',{"msg":"อีเมล์ใช้งานไปแล้ว หรือ ผู้ใช้ซํ้า"})
            else:
                user = User.objects.create_user(username=username,email =  email,password = pwd)
                # User.objects.create(email=email,password=pwd)
                return redirect('login')
        else:    
            return render(request, 'pages/register.html',{"msg":"มีความผิดพลาด"})
        
    return render(request,'pages/register.html')

def logout(request):
    
    auth.logout(request)
    return redirect('index')

def job(request,id):

    job = Job.objects.get(id=id)
    return render(request, 'pages/job.html',{"job":job})

def upload_file(request):
    if request.method == "POST":
        file = UploadFile(request.POST,request.FILES)
        if file.is_valid():
            file = request.FILES['file']
            print(file.name,file.content_type)
    form =UploadFile()
    return render(request, 'pages/upload_file.html',{'form':form})