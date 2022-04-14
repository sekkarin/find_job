from django.shortcuts import render , HttpResponse ,redirect
from app.models import User
# Create your views here.
def index(request):
    
    return render(request, 'pages/index.html')

def login(request):
    
    return render(request,'pages/login.html')
def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        check_service = request.POST.get('check_service')
        print(email,pwd,check_service)
        return redirect('index')
        
    return render(request,'pages/register.html')
