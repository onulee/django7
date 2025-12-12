from django.shortcuts import render
from django.http import HttpResponse

# 메인페이지 호출
def index(request):
    error = request.GET.get('error')
    context = {"error":error}
    return render(request,'index.html',context)
