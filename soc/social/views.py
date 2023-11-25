from django.shortcuts import render, redirect
from social.models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')

def reg(request):
    suc = 0
    if request.method == 'POST':
        fio = request.POST['fio']
        login = request.POST['login']
        password = request.POST['password']
        date = request.POST['date']
        city = request.POST['city']
        if User.objects.filter(login=login).exists():
            suc=2
        else:
            user = User()
            user.fio = fio
            user.login = login
            user.password = password
            user.date = date
            user.city = city
            user.save()
            suc = 1
    return render(request, 'reg.html', context={'suc': suc})

def auth(request):
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        if User.objects.filter(login=login).exists() and User.objects.filter(password=password):
            request.session['login'] = login
    return render(request, 'auth.html')

def logout(request):
    if 'login' in request.session:
        del request.session['login']
    return redirect('/')


def users(request):
    users = User.objects.all()
    return render(request, 'users.html', context={'users': users})

def userid(request, id):
    if User.objects.filter(id=id).exists():
        user = User.objects.filter(id=id).first()
        return render(request, 'userid.html', context={'user': user})
    else:
        return redirect('/')



