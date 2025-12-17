from django.shortcuts import render
from comment.models import Comment
from board.models import Board
from member.models import Member
from django.http import JsonResponse,HttpResponse # 전송할때 Json타입으로 변경해서 전송
from django.core import serializers  # Json타입으로 전달된 데이터를 파이썬데이터(set)로 변경


# 하단댓글 부분 
def clist(request):
    bno = request.GET.get('bno') 
    print("bno : ",bno)
    board = Board.objects.get(bno=bno)
    qs = Comment.objects.filter(board=board)
    list_qs = list(qs.values())  # QuerySet → 리스트
    context = {'result': 'success','list':list_qs}
    return JsonResponse(context)

   