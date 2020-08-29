from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
# Create your views here.

def signup(request):
    regi_form = UserCreationForm()
    if request.method == "POST":
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index')

    return render(request, 'signup.html',{'regi_form':regi_form})

# django 문서의 LoginView를 MyLoginView로 상속받아서 오버라이딩
class MyLoginView(LoginView):
    template_name = 'login.html'
