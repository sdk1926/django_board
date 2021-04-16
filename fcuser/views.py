from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

   

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    
    return redirect('/')

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
        
    else:    
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':    
        # input태그의 네임을 키로 갖는다. 즉 각 인풋에 들어온값을 표현한다. 
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        
        res_data = {}

        if not (username and password and re_password and useremail):
            res_data['error'] = '모든값을 입력해야 합니다.'

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                username=username,
                password=make_password(password),   # make_password함수를 사용해서 암호화하고 저장 
                useremail=useremail
            )

            fcuser.save()

        return render(request, 'register.html', res_data) # resdata에담긴 변수가 html코드로 변경되서 전달 

