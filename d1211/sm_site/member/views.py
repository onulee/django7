from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Member

# 로그인
def login(request):
    if request.method == 'GET':
        return render(request,'member/login.html')
    elif request.method == 'POST':
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        print("post 입력 : ",id,pw)
        qs = Member.objects.filter(id=id,pw=pw)
        if qs:
            print("아이디와 비밀번호가 일치합니다.")
            context = {"error":"1"}
            return render(request,'member/login.html',context)
        else:
            print("아이디와 비밀번호가 일치하지 않습니다.")    
            context = {"error":"0"}
            return render(request,'member/login.html',context)

#------------------------------------------------------
# 회원전체리스트페이지
def list(request):
    qs = Member.objects.all().order_by('-mdate')
    context = {"list":qs}
    return render(request,'member/list.html',context)


# 회원등록페이지
def write(request):
    if request.method == 'GET':
        return render(request,'member/write.html')
    elif request.method == 'POST':
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")
        hobby = request.POST.getlist("hobby")
        Member.objects.create(
           id=id,pw=pw,name=name,phone=phone,gender=gender,hobby=hobby 
        )
        # qs = Member(id=id,pw=pw,name=name,phone=phone,gender=gender,hobby=hobby)
        # qs.save()
        print("post 확인 : ",id)
        return redirect('/')