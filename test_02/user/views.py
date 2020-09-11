from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from user.models import UserInfo
from django.urls import reverse

import re
# Create your views here.

def login_required(view_func):
    '''登录判断装饰器'''
    def wrapper(request, *args, **kwargs):
        if request.session.has_key('islogin'):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/user/login')
    return wrapper

@login_required
def index(request):
    return render(request, 'user/index.html')


def login(request):
    # 通过session判断是否已经登录
    if request.session.has_key('islogin'):
        print(request.session.get('islogin'))
        url = reverse('user:index')
        return redirect(url)
    else:
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request, 'user/login.html', {'username': username})


def login_config(request):
    ret = False
    user_list = UserInfo.objects.all()
    username = request.POST.get('username')
    password = request.POST.get('password')
    isRemember = request.POST.get('remember')
    print(isRemember)
    for user in user_list:
#        print(user.uname, type(user.uname))
#        print(username, type(username))
        if (user.uname == username) & (user.upassword == password):
            response = redirect('/user/index')
            if isRemember == 'on':
                # 设置cookie
                response.set_cookie('username', username, max_age=10)
            # 设置session
            request.session['islogin'] = True
            return response

    return redirect('/user/login')


def register(request):

    return render(request, 'user/register.html', {})


def register_config(request):
    u = UserInfo()
    username = request.POST.get('username')
    password = request.POST.get('password')
    pwd_config = request.POST.get('pwd_config')
    ret1 = re.match(r"^[a-zA-Z0-9_]{4,20}@(126|163|qq|sina|gmail)\.com$", username)
    print(ret1)
    ret2 = re.match(r"(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z]).{6,18}", password)
    print(ret2)
    if not ret1:
        return HttpResponse('账号格式不对')
    elif not ret2:
        return HttpResponse('密码格式不对')
    elif password != pwd_config:
        return HttpResponse('两次密码不同')
    else:
        try:
            u.uname = username
            u.upassword = password
            u.save()
        except Exception as e:
            print(e)
            return HttpResponse("该账号已经存在！")
        else:
            return HttpResponse('register success')


def ajax_login(request):
    return render(request, 'user/ajax_login.html')


def login_ajax_handle(request):
    user_list = UserInfo.objects.all()
    username = request.POST.get('username')
    password = request.POST.get('password')
    for user in user_list:
        print(user.uname, type(user.uname))
        print(username, type(username))
        if (user.uname == username) & (user.upassword == password):
            return JsonResponse({'res': 1})

    return JsonResponse({'res': 0})


def logout(request):
    request.session.clear()
    return render(request, 'user/logout.html')


def logout_flush(request):
    request.session.flush()
    return render(request, 'user/logout_flush.html')


def url_reverse(request):
    return render(request, 'user/url_reverse.html')


