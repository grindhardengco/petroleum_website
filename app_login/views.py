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
    User.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        company = request.POST['company'],
        password = hashed_pw
    )
    user = User.objects.get(email = request.POST['email'])
    messages.success(request, "Thank you for registering! Please log in to enjoy the features of our website.")
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
    request.session['name'] = user.name
    request.session['email'] = user.email
    request.session['company'] = user.company

    if user.email == 'admin@superiorpetro.com':
        return redirect ('/superior/admin')
    return redirect('/success_login')

def success_login(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in to view this page.")
        return redirect('/')
    
    return render(request, 'success_login.html')

def edit_account(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in to view this page.")
        return redirect('/')
    
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'edit_account.html', context)

def update_account(request):
    errors=User.objects.edit_validator(request.POST, request.session)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/edit_account')
    
    user = User.objects.get(id=request.session['user_id'])
    
    if len(request.POST['password']) != 0:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode()
        user.password = hashed_pw

    user.name = request.POST['name']
    user.email = request.POST['email']
    user.company = request.POST['company']
    user.save()
    messages.success(request, "Account update was successful.")
    request.session['name'] = user.name
    request.session['email'] = user.email
    request.session['company'] = user.company
    return redirect('/edit_account')

def logout(request):
    request.session.clear()
    messages.success(request, "You are logged out.  Thank you for visiting.  We hope you enjoy the rest of your day!")
    return redirect('/superior/home')