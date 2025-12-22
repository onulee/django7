from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

from home.models import ChartData

def index(request):
    return render(request,'main.html')

def my_map(request):
    return render(request,'my_map.html')

def chart2(request):
    return render(request,'chart2.html')


# @csrf_exempt  # csrf_token 예외처리
# 단순데이터 처리
def chart_json(request):
    context = {'dd_data':[10, 5, 9, 8, 3, 6],'ll_data':['홍길동','유관순','이순신','강감찬','김구','김유신']}
    return JsonResponse(context)

# db데이터 처리
def chart_json2(request):
    qs = ChartData.objects.all()
    l_qs = list(qs.values()) 
    
    context = {'list_data':l_qs}
    return JsonResponse(context)
