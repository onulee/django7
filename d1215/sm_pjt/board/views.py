from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Board
from member.models import Member

# 게시글 수정
def update(request,bno):
    if request.method == 'GET':
        print("수정url : ",bno)
        # Board테이블에서 bno=1 
        qs = Board.objects.get(bno=bno)
        context = {'board':qs}
        return render(request,'board/update.html',context)
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        id = request.session['session_id']
        # 수정저장이 완료되면
        qs = Board.objects.get(bno=bno)
        qs.btitle = btitle
        qs.bcontent = bcontent
        qs.save()
        context ={'flag':1}
        return render(request,'board/update.html',context)
        

# 게시글 삭제
def delete(request,bno):
    print("url : ",bno)
    # Board테이블에서 bno=1 
    qs = Board.objects.get(bno=bno)
    qs.delete()
    return redirect('/board/list/')

# 게시글 상세보기
def view(request,bno):
    print("url : ",bno)
    # Board테이블에서 bno=1 
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request,'board/view.html',context)


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
        
