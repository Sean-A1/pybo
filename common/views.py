from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from common.forms import UserForm

def logout_view(request):
    logout(request)
    return redirect('index')

def signup(request):
    if request.method == "POST": # POST 요청인 경우에는 화면에서 입력한 데이터로 사용자를 생성
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # form.cleaned_data.get은 폼의 입력값을 개별적으로 얻고 싶은 경우에 사용하는 함수
            # 이 경우 폼의 입력값은 인증시 사용할 사용자명과 비밀번호
            
            # 신규 사용자를 생성한 후에 자동 로그인
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else: # GET 요청인 경우에는 회원가입 화면을 보여준다
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def page_not_found(request, exception):
    return render(request, 'common/404.html', {})