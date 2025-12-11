from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Member

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