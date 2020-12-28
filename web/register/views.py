from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):

    userform = UserCreationForm()

    if request.method == 'POST':
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect('<h1>ok</h1>')


    context = {
        'form':userform
    }

    return render(request, 'register.html', context)
