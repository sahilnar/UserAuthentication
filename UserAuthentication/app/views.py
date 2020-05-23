from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
# Create your views here.
def index(req):
    return render(req,'index.html')

def signup(req):
    if req.method == 'POST':
        form = SignUpForm(req.POST)
        if form.is_valid():
            user = form.save()
            auth_login(req, user)
            return redirect('index')
    else: 
        form = SignUpForm()
    return render(req, 'signup.html', {'form':form})