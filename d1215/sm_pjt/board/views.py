from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
from member.models import Member

# 게시판리스트
def list(request):
    qs = Board.objects.all().order_by('-bno')
    print(qs)
    context = {'list':qs}
    return render(request,'board/list.html',context)

# 글쓰기화면/글쓰기저장
def write(request):
    if request.method == 'GET':
        return render(request,'board/write.html')
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        id = request.session['session_id']
        # member객체를 저장해야 함.
        qs = Member.objects.get(id=id)
        Board.objects.create(btitle=btitle,bcontent=bcontent,member=qs)
        
        context = {'flag':'1'}
        return render(request,'board/write.html',context)
        
