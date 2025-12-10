from django.shortcuts import render,redirect
from .models import Student

# 학생등록함수
def write(request):
    if request.method == 'GET':
        return render(request,'student/write.html')
    elif request.method == 'POST':
        # form폼에서 넘어온 데이터 처리
        
        
        return redirect('/')

# 학생리스트함수
def list(request):
    # db명령어 - select,insert,update,delete
    qs = Student.objects.all()
    # qs = Student.objects.get(name='홍길동')
    # qs2 = Student.objects.get(name='유관순')
    context = {"list":qs}
    return render(request,'student/list.html',context)
