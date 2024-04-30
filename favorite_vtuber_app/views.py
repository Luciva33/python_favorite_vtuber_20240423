from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

# アカウント登録
def signupfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'login.html')
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザは既に登録されています'})

    return render(request, 'signup.html')

def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('top')
        else:
            return render(request, 'login.html', {'error': 'ログイン情報が正しくありません'})
        
    return render(request, 'login.html', {})