from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def post_list():
    pass

# 회원가입
# 1. url pattern view 추가
# 2. 여기다가 해당하는 함수 만들기

def signup():
    # email nickname password 검증
    # if email이 db에 존재하는지 ?
    user = User.objects.create_user(nickname, email, password)
    if not u:
    #   NO : 회원가입 진행시켜
        pass
    #   YES : login

    #       password 암호화
    #       db에 넣어
    #       response 보내
    pass

def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # redirect to a success page.
    else:
        # return an 'invalid login' error message.
        pass

    # email password 검증
    # if email이 db에 존재하는지 ?
    #   YES : login
    #   NO : 회원가입 시켜
    pass

def signout(request):
    logout(request)
    # redirect to a success page.




