from django.shortcuts import render, redirect, get_object_or_404
from .models import *
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
        friend = get_object_or_404(User, id=id)
        current_user = get_object_or_404(User, login=request.session['login'])
        current_user_friends = Friend.objects.filter(user=friend)





        suc = 0

        if Friend.objects.filter(user=current_user, friend=friend).exists():
            suc = 1
        r = 0
        userf = User.objects.filter(login=request.session['login']).first()


        mypages = Mypage.objects.filter(user=user)
        return render(request, 'userid.html', context={'user': user, 'suc': suc, 'user_id': userf.id, 'id': id, 'current_user_friends': current_user_friends, 'mypages': mypages})
    else:
        return redirect('/')



def add_chat(request, id):
    friend = get_object_or_404(User, id=id)
    concurrent_user = get_object_or_404(User, login=request.session['login'])
    if request.method == 'POST':
        message = request.POST['message']
        Chat.objects.create(user=concurrent_user, friend=friend, message=message)

    return render(request, "user/chat.html")
def add_friend(request):
    friend = get_object_or_404(User, id=request.POST['friend'])

    current_user = get_object_or_404(User, login=request.session['login'])

    if friend==current_user:
        return redirect('/user/'+request.POST['friend'])

    if not Friend.objects.filter(user=current_user,friend=friend).exists():
        Friend.objects.create(user=current_user, friend=friend)
    return redirect('/user/'+request.POST['friend'])

def mypage(request):
    current_user = get_object_or_404(User, login=request.session['login'])
    friend = get_object_or_404(User, id=current_user.id)
    current_user_friends = Friend.objects.filter(user=friend)

    if request.method =="POST":
        message = request.POST['message']
        Mypage.objects.create(user=current_user, message=message)
        return redirect('/mypage/')


    mypages = Mypage.objects.filter(user=current_user)
    return render(request, 'user/mypage.html',  {'current_user': current_user, 'current_user_friends': current_user_friends, 'mypages': mypages})


def deleteuserid(request, id):
    Friend.objects.filter(id=id).delete()

    return redirect('/mypage')

def deletemypage(request):
    if request.method == 'POST':
        id = request.POST['id']
        Mypage.objects.filter(id=id).delete()
    return redirect('/mypage/')