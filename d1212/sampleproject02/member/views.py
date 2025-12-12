from django.shortcuts import render
from .models import Member
from django.http import HttpResponse

# 로그인 부분
def login(request):
    return render(request,'member/login.html')
        
# 로그인 부분
def logout(request):
    return render(request,'member/login.html')