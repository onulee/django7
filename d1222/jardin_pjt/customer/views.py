from django.shortcuts import render,redirect
from django.http import JsonResponse
from customer.models import Board
from member.models import Member
from django.core.paginator import Paginator
from django.db.models import F,Q,Sum,Count
from comment.models import Comment

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#### 좋아요 추가 : ajax
def clikes(request):
    if request.method == 'POST':
        bno = request.POST.get('bno')
        board = Board.objects.get(bno=bno)
        id = request.session['session_id']
        member = Member.objects.get(id=id)
        
        # board.likes.all() : 게시글에 좋아요를 클릭한 전체회원
        # member.likes_member.all() : 현재회원이 좋아요를 클릭한 게시글 전체목록
        # db : Board테이블에 likes컬럼에 데이터 추가,삭제
        if board.likes.filter(pk=member.id).exists():
            board.likes.remove(member) # likes 안에 member를 제거
            result = '삭제'
        else:
            board.likes.add(member)    # likes 안에 member를 추가
            result = '추가'    
        count = board.likes.count()    # 좋아요 개수    
    print('좋아요 개수 확인 : ',count)
    print('result : ',result)
    context = {'result':result,'count':count}
    return JsonResponse(context)


def cwrite(request):
    if request.method == 'GET':
        return render(request,'customer/cwrite.html')
    elif request.method == 'POST':
        id = request.session['session_id']
        member = Member.objects.get(id=id)
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        # db에 저장
        qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
        qs.bgroup = qs.bno
        qs.save()
        return redirect('/customer/clist/')
        

# 고객센터 페이지 뷰 ----------------------------
# Board : 좋아요도 포함되어 전달됨.
def cview(request,bno):
    # 1개 게시글
    qs = Board.objects.get(bno=bno)
    # 하단댓글
    comment_qs = Comment.objects.all().order_by('-cno')
    
    # bgroup 역순정렬, bstep 순차정렬
    #이전글-----
    pre_qs = Board.objects.filter(bgroup__lt=qs.bgroup).order_by("-bgroup","bstep").first()
    # 답글달기가 포함 되어 있을때 쿼리문
    # pre_qs = Board.objects.filter(Q(bgroup__lt=qs[0].bgroup,bstep__lte=qs[0].bstep)|Q(bgroup=qs[0].bgroup,bstep__gt=qs[0].bstep)).order_by("-bgroup","bstep").first()
    print("이전글 : ",pre_qs)
    #다음글-----
    next_qs = Board.objects.filter(bgroup__gt=qs.bgroup).order_by('bgroup','-bstep').first()
    # 답글달기가 포함 되어 있을때 쿼리문
    # next_qs = Board.objects.filter(Q(bgroup__gt=qs[0].bgroup,bstep__gte=qs[0].bstep)|Q(bgroup=qs[0].bgroup,bstep__lt=qs[0].bstep)).order_by("bgroup","-bstep").first()
    print("다음글 : ",next_qs)

    context = {'c':qs,'pre_c':pre_qs,'next_c':next_qs,'comment_qs':comment_qs}
    return render(request,'customer/cview.html',context)

def clist(request):
    # 검색부분-------------------------------------------------
    category = request.GET.get('category','')
    search = request.GET.get('search','')
    print("검색으로 넘어온 데이터 : ",category,search)
    #--------------------------------------------------------
    if not search:
        qs = Board.objects.all().order_by('-bgroup','bstep')
    else:
        if category == 'btitle':
            qs = Board.objects.filter(btitle__contains=search)
        elif category == 'bcontent':
            qs = Board.objects.filter(bcontent__contains=search)
        elif category == 'all':
            qs = Board.objects.filter(Q(btitle__contains=search)|Q(bcontent__contains=search))
    
    # 하단페이지 넘버링-----------------------------------------
    # Pagenator는 꼭 요청페이지 번호가 있어야 함.
    # 요청페이지번호 : int타입
    page = int(request.GET.get('page',1)) # 없으면 1번 페이지 호출
    paginator = Paginator(qs,7)
    list_qs = paginator.get_page(page)
    # -------------------------------------------------------
    
    context = {'list':list_qs,'page':page,'category':category,'search':search}
    return render(request,'customer/clist.html',context)



# -----------------------------------------------
# [ 하단넘버링 ]
# * 이전페이지 유무 : {% if list.has_previous %}


#-----------------------------------------------------------------------
# json
#-----------------------------------------------------------------------
# 게시판 리스트
@api_view(['GET'])    
def clistJson(request):
    
    # DRF형태
    # axios Json데이터로 전달
    id = request.data.get('id')
    name = request.data.get('name')
    print('get id,name : ',id,name)
    qs = Board.objects.all()
    l_qs = list(qs.values())
    context = {'list':l_qs}
    return Response(context, status=status.HTTP_200_OK)

# 고객센터 페이지 뷰 ----------------------------
@api_view(['GET'])  
def cviewJson(request,bno):
    # bgroup 역순정렬, bstep 순차정렬
    qs = list(Board.objects.filter(bno=bno).values())
    print("qs 데이터 형태 : ",qs[0])
    context = {'board':qs[0]}
    return Response(context, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def cdeleteJson(request,bno):
    name = request.data.get('name','')
    print('넘어온 데이터 bno : ',bno)
    print('넘어온 데이터 name : ',name)
    Board.objects.get(bno=bno).delete()
    context = {'result':'성공'}
    return Response(context, status=status.HTTP_200_OK)

@api_view(['POST'])
def cwriteJson(request):
    # list타입으로 변경을 해서 Json타입으로 변경을 해야 함.
    # objects.filter(), objects.all() -> list타입
    id = request.data.get('id','')
    member = Member.objects.get(id=id)
    btitle = request.data.get('btitle')
    bcontent = request.data.get('bcontent')
    # bfile = request.FILES.get('bfile')
    print('넘어온데이터 id,btitle,bcontent : ',id,btitle,bcontent)
    bfile =''
    # db에 저장
    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()
    
    l_qs = list(Board.objects.filter(bno=qs.bno).values())
    print("l_qs 데이터 형태 : ",l_qs)
    context = {'result':'성공','board':l_qs}
    # context = {'result':'성공'}
    return Response(context, status=status.HTTP_200_OK)