from django.shortcuts import render

# 성적입력페이지 열기
def write(request):
    return render(request,'write.html')
