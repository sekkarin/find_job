from django.shortcuts import render , HttpResponse ,redirect ,HttpResponseRedirect 
from django.http import JsonResponse
# from app.models import User
from django.contrib.auth.models import User ,auth
from django.contrib.auth import authenticate
from company.models import *
from .forms import UploadFile
from app.models import *

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator

from django.views.generic.base import TemplateView


# Create your views here.
class Job_app(TemplateView):
    template_name = "pages/job_app.html"

class MyWork(TemplateView):
    # pk=kwargs['pk']
    # print(pk)
    template_name = "pages/my_works.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(kwargs['id'])
        context['datas'] = My_work.objects.filter(user_id = kwargs['id'])
        # print(context['datas'].values())
        return context
    
class JobGroup(TemplateView):
    # pk=kwargs['pk']
    # print(pk)
    template_name = "pages/group_job.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(kwargs['id'])
        context['datas'] = Job.objects.filter(id_type = kwargs['id'])
        print(context['datas'].values())
        return context

def index(request):
    jobs = Job.objects.all()
    job_count = jobs.count()
    jobs = jobs.order_by('-id')[0:8]
    type_job = Type_job.objects.all()
    
    return render(request, 'pages/index.html',{"jobs":jobs,"totle_job":job_count,'type_job':type_job})

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

def like_job(request,id_user,id_job):
    job = Job.objects.get(id=id_job)
    user = User.objects.get(id=id_user)
    print(id_user,id_job)
    work = My_work(user=user,job_id=job)
    work.save()

    return JsonResponse({'status':200})
        

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']

            #เปิดไฟล์ในโฟลเดอร์ media ตามที่ได้สร้างเอาไว้ โดยใช้ชือเดียวกับไฟล์ที่อัปโหลดขึ้น
            #เพื่อเขียน (w) ในโหมดไบนารี (b) ถ้ายังไม่มีอยู่ก่อน ให้สร้างขึ้นใหม่ (+)
            with open(f'media/upload/{file.name}', 'wb+') as target:
                #แบ่งไฟล์เป็นส่วนย่อยๆ แล้วนำมาเขียนลงในไฟล์เป้าหมายต่อเนื่องกันจนครบ
                for chunk in file.chunks():
                    target.write(chunk)

                #หรืออ่านเนื้อหาของไฟล์ทั้งหมด แล้วเขียนพร้อมกันทีเดียว
                #โดยไม่ต้องใช้ลูป for แต่ไม่ควรกับไฟล์ที่มีขนาดใหญ่
                #target.write(f.read())

        else:
            file = None

    else:
        form = UploadFile()
        file = None
    
    return render(request, 'pages/upload_file.html', {'form':form, 'file':file})

def simple_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploadfile')
    else:
        form = DocumentForm()
    data = Document.objects.get(id=4)
    return render(request, 'pages/upload_file.html', {'form': form,'data':data})