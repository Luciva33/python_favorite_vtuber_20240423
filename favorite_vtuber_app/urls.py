from django.urls import path
from .views import signupfunc, loginfunc, topfunc, registerCharacterfunc, logoutfunc, registerCharacterConfirmfunc, detailCharacterfunc

urlpatterns = [
    path('signup/', signupfunc, name = 'signup'),
    path('login/', loginfunc, name = 'login'),
    path('top/', topfunc, name = 'top'),
    path('detail-character/<int:pk>', detailCharacterfunc, name = 'detail-character'),
    path('register-character/', registerCharacterfunc, name = 'register-character'),
    path('register-character-confirm/<int:pk>', registerCharacterConfirmfunc, name = 'register-character-confirm'),
    path('logout/', logoutfunc, name = 'logout'),
]
