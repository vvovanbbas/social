from django.shortcuts import render
from social.models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')

def reg(request):
    if request.method == 'POST':
        fio = request.POST['fio']
        login = request.POST['login']
        password = request.POST['password']
        date = request.POST['date']
        city = request.POST['city']

        user = User()
        user.fio = fio
        user.login = login
        user.password = password
        user.date = date
        user.city = city
        user.save()
    return render(request, 'reg.html')

def auth(request):
    if request.method == 'POST':
        login = request.POST['login1']
        password = request.POST['password1']

        user = User_1()
        user.login = login
        user.password = password
    return render(request, 'auth.html')

