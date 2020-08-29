from django.contrib import admin
from django.urls import path
from .views import signup, MyLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('signup/', signup, name="signup"),
   path('login/', MyLoginView.as_view(), name="login"), # LoginView 클래스를 함수로 실행
   path('logout/', LogoutView.as_view(), name="logout"),
]
