import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import MVtubers, TFavoriteVtubers, MVtubersProfiles
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

# お気に入りキャラ詳細
@login_required
def detailCharacterfunc(request, pk):
    vtuber_instance = MVtubers.objects.get(id = pk)
    mVtuber = get_object_or_404(TFavoriteVtubers, user=request.user, vtuber=vtuber_instance)

    mVtubersProfiles = MVtubersProfiles.objects.filter(vtuber = vtuber_instance)

    # mp4かgifか判定
    introduction_video_url = mVtuber.vtuber.introduction_video_url
    is_video = False
    if introduction_video_url and introduction_video_url.endswith('.mp4'):
        is_video = True

    # 動画のサムネイル取得
    video_urls = [
        mVtuber.vtuber.recommended_video1,
        mVtuber.vtuber.recommended_video2,
        mVtuber.vtuber.recommended_video3
    ]
    thumbnails = []
    for url in video_urls:
        if url:
            thumbnail_url = generate_thumbnail(url)
            thumbnails.append(thumbnail_url)

    return render(request, 'detail-character.html', {'mVtuber' : mVtuber, 'is_video': is_video, 'thumbnails' : thumbnails, 'mVtubersProfiles' : mVtubersProfiles})

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
    
# YouTubeの動画URLから動画IDを抽出し、サムネイルのURLを生成する関数
def generate_thumbnail(video_url):
    video_id = re.search(r"(?:\?v=|\/embed\/|\.be\/)([\w-]+)", video_url).group(1)
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    return thumbnail_url