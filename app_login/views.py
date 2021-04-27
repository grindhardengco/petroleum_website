from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):

    return render(request, 'index.html')

def register(request):
    errors=User.objects.user_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    
    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode()
    print(hashed_pw)
    User.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        password = hashed_pw
    )
    user = User.objects.get(email = request.POST['email'])
    request.session['user_id'] = user.id
    request.session['user_name'] = user.first_name
    messages.success(request, "Thank you for registering!")
    return redirect('/')

def success_reg(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in to view this page.")
        return redirect('/')
    
    return render (request, 'success_reg.html')

def login(request):    
    try:
        user = User.objects.get(email = request.POST['email'])
        pass
    except:
        messages.error(request, "Email has not yet been registered.")
        return redirect('/')

    if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        messages.error(request, "This password does match our records.")
        return redirect ('/')

    request.session['user_id'] = user.id
    request.session['user_name'] = user.name
    
    return redirect('/success_login')


def success_login(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in to view this page.")
        return redirect('/')
    
    return render(request, 'success_login.html')

def logout(request):
    request.session.clear()
    return redirect('/superior')