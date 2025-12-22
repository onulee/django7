from django.shortcuts import render
from django.http import JsonResponse

def step03(request):
    return render(request,'member/step03.html')

# json 리턴 : id가 존재하는지 확인
def idCheck(request):
    # db확인
    
    #----------------
    context = {'result':'사용가능'}
    return JsonResponse(context)
