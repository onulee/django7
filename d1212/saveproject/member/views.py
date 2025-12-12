from django.shortcuts import render,redirect

def login(request):
    if request.method == 'GET':
        cook_id = request.COOKIES.get("cook_id","")
        context = {"cook_id":cook_id}
        return render(request,'member/login.html',context)
    elif request.method == 'POST':
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        login_keep = request.POST.get("login_keep")
        # 쿠키 읽기
        print("모든 쿠키 읽기 : ",request.COOKIES)
        # 쿠키저장
        response = redirect("/")
        if login_keep:
            print("쿠키를 저장.")
            response.set_cookie("cook_id",id)
        else:
            print("쿠키를 삭제.")  
            response.delete_cookie("cook_id")  
        print("post 입력된 데이터 : ",id,pw,login_keep)
        return response
        
