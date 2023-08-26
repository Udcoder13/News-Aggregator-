from typing import Any, Dict
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from.import forms
from .forms import UserForm
from Newss.views import NewsList
from django.contrib.auth import login,logout,authenticate
from Newss.views import index
def Register(request):
    if request.method == 'POST':
       userform=UserForm(request.POST)
       if userform.is_valid():
          userform.save()
          return redirect('login')
    else:
        userform = UserForm()

    return render(request,'account/registration.html',{'userform':userform})

def Logout(request):
    logout(request)
    return redirect('index')
      