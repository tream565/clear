from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from login.forms import LoginForm

# Create your views here.
def ok(request):
    return render(request,'login_success.html')

def log_out(request):
    logout(request)
    return render(request,'logout_success.html')

def sign_in(request):
    form = LoginForm()
    if request.method == 'POST':
        username =request.POST.get("username")
        password =request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/login/ok')


    context = {
        'form': form
    }
    return render(request, 'login.html', context)