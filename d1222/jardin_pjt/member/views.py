from django.shortcuts import render
from django.http import JsonResponse
from member.models import Member

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
