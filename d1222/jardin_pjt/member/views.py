from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from member.models import Member

def logout(request):
    # 섹션 모두 삭제
    request.session.clear()
    
    return redirect('/')

# 로그인 부분
def login(request):
    if request.method == 'GET':
        return render(request,'member/login.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        print("넘어온 데이터 : ",id,pw)
        
        # id,pw체크
        qs = Member.objects.filter(id=id,pw=pw)
        if qs: 
            result = 1    
            request.session['session_id'] = id
            request.session['session_name'] = qs[0].name
        else: result = 0
        context = {'result':result}
        
        return render(request,'member/login.html',context)
        

# 회원가입
def step03(request):
    return render(request,'member/step03.html')

# json 리턴 : id가 존재하는지 확인
def idCheck(request):
    # db확인
    id = request.GET.get('id','')
    qs = Member.objects.filter(id=id)
    if not qs: result = '사용가능'
    else: result = '사용불가'    
    #----------------
    context = {'result':result}
    return JsonResponse(context)

# json 리턴 : user전체리스트
@api_view(['GET'])
def userAll(request):
    
    # DRF형태
    id = request.data.get('id')
    name = request.data.get('name')
    print('get id,name : ',id,name)
    
    # axios Json데이터로 전달
    # print('id : ',request.GET.get('id',''))
    # print('name : ',request.GET.get('name',''))
    qs = Member.objects.all()
    l_qs = list(qs.values())
    #print("l_qs 데이터 형태 : ",l_qs)
    context = {'arr':l_qs}
    return JsonResponse(context)

# json 리턴 : user 추가
# @csrf_exempt
@api_view(['POST'])
def userInsert(request):
    # DRF형태
    id = request.data.get('id')
    name = request.data.get('name')
    print('post id,name : ',id,name)
    
    # axios에서 넘어온 데이터는 json데이터
    # body = json.loads(request.body)
    # id = body.get('id')
    # print("id : ",id)
        
    qs = Member.objects.all()
    l_qs = list(qs.values())
    context = {'arr':l_qs}
    return JsonResponse(context)


# json 리턴 : user 수정
@api_view(['PUT'])
def userUpdate(request):
    # DRF형태
    id = request.data.get('id')
    name = request.data.get('name')
    print('put id,name : ',id,name)
    
    qs = Member.objects.all()
    l_qs = list(qs.values())
    context = {'arr':l_qs}
    return JsonResponse(context)

# json 리턴 : user 수정
@api_view(['DELETE'])
def userDelete(request):
    # DRF형태
    id = request.data.get('id')
    name = request.data.get('name')
    print('delete id,name : ',id,name)
    
    qs = Member.objects.all()
    l_qs = list(qs.values())
    context = {'arr':l_qs}
    return JsonResponse(context)
