from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import MVtubers, TFavoriteVtubers
from django.contrib.auth.models import User
from django.db import IntegrityError

# アカウント登録
def signupfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
    
        try:
            user = User.objects.create_user(username, '', password)
            login(request, user)
            return redirect('top')
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザは既に登録されています'})
    
    return render(request, 'signup.html')

# ログイン
def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # ログイン成功
            return redirect('top')
        else:
            return render(request, 'login.html', {'error': 'ログイン情報が正しくありません'})
        
    return render(request, 'login.html')

# ログアウト
def logoutfunc(request):
    logout(request)
    return redirect('login')

# トップ
@login_required
def topfunc(request):
    tFavoriteVtubers = TFavoriteVtubers.objects.filter(user=request.user)
    return render(request, 'top.html', {'tFavoriteVtubers' : tFavoriteVtubers})

@login_required
def detailCharacterfunc(request, pk):
    vtuber_instance = MVtubers.objects.get(id = pk)
    mVtuber = get_object_or_404(TFavoriteVtubers, user=request.user, vtuber=vtuber_instance)
    return render(request, 'detail-character.html', {'mVtuber' : mVtuber})

# お気に入りキャラ登録
@login_required
def registerCharacterfunc(request):
    mVtubers = MVtubers.objects.all()
    return render(request, 'register-character.html', {'mVtubers' : mVtubers})


# お気に入りキャラ登録確認
@login_required
def registerCharacterConfirmfunc(request, pk):
    if request.method == "POST":
        vtuber_instance = MVtubers.objects.get(id = pk)

        favorite_vtuber = TFavoriteVtubers(user = request.user, vtuber = vtuber_instance)
        favorite_vtuber.save()

        return redirect('top')
    else:
        mVtuber = get_object_or_404(MVtubers, pk = pk)
        return render(request, 'register-character-confirm.html', {'mVtuber' : mVtuber})